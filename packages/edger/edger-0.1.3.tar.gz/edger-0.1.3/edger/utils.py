import win32gui
import win32con
import logging
import time
import win32process
import psutil
import pyautogui
import pyperclip
import urllib.parse
import os
from PIL import Image
import subprocess
import ctypes
from ctypes import wintypes
import threading
import jiggler as Jiggler  # Capitalize the module alias for consistency

# Reference to the update menu function from edger.py
update_menu_function = None

def set_system_tray_icon(update_menu_func):
    """Sets the reference to the system tray icon's update_menu function."""
    global update_menu_function
    update_menu_function = update_menu_func
    
    # Also set it for the jiggler module
    Jiggler.set_menu_updater(update_menu_function)

def activate_window(hwnd):
    """Bring a window to the foreground if it's not minimized."""
    try:
        if win32gui.IsIconic(hwnd):
            win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
        time.sleep(0.2)
        win32gui.SetForegroundWindow(hwnd)
        time.sleep(0.3)
    except Exception as e:
        logging.error(f"Could not activate window: {e}")

def make_transparent(hwnd):
    """Makes the window transparent."""
    try:
        # Set the window to layered style (required for transparency)
        style = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
        win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, 
                             style | win32con.WS_EX_LAYERED)
        
        # Set transparency level (0 = fully transparent, 255 = fully opaque)
        win32gui.SetLayeredWindowAttributes(hwnd, 0, 0, win32con.LWA_ALPHA)
        logging.info(f"Made window transparent: {hwnd}")
    except Exception as e:
        logging.error(f"Could not make window transparent: {e}")

def get_edge_windows():
    """Find all Microsoft Edge windows."""
    edge_windows = []

    def callback(hwnd, _):
        if win32gui.IsWindowVisible(hwnd):
            _, pid = win32process.GetWindowThreadProcessId(hwnd)
            try:
                process_name = psutil.Process(pid).name().lower()
                if "msedge" in process_name:
                    edge_windows.append(hwnd)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass

    win32gui.EnumWindows(callback, None)
    return edge_windows

def get_edge_url(hwnd, bypass_list):
    """Extracts URL from Edge's address bar, handling bypass URLs."""
    try:
        activate_window(hwnd)
        
        # Make the window transparent immediately after activation
        make_transparent(hwnd)
        
        pyautogui.hotkey("ctrl", "l")
        pyautogui.hotkey("ctrl", "c")
        url = get_clipboard()

        if url and url.startswith("http"):
            if any(bypass_url in url for bypass_url in bypass_list):
                logging.info(f"Detected bypass URL: {url}, waiting for redirection...")
                url = wait_for_redirect(url)
            return url

        logging.error("Could not extract a valid URL.")
    except Exception as e:
        logging.error(f"Failed to extract URL: {e}")
    return None

def get_clipboard():
    """Retrieves clipboard contents, retrying once if initially empty."""
    text = pyperclip.paste().strip()
    if not text:
        time.sleep(0.1)
        text = pyperclip.paste().strip()
    return text or None

def wait_for_redirect(original_url, timeout=5):
    """Waits for a URL to change within a timeout."""
    start_time = time.time()
    while time.time() - start_time < timeout:
        time.sleep(0.2)
        pyautogui.hotkey("ctrl", "l")
        pyautogui.hotkey("ctrl", "c")
        new_url = get_clipboard()

        if new_url and new_url != original_url and new_url.startswith("http"):
            logging.info(f"Redirected URL detected: {new_url}")
            return new_url

    logging.warning(f"Redirection timeout, using original URL: {original_url}")
    return original_url

def convert_bing_to_alternative(url, search_engine_url):
    """Converts Bing search URLs to the alternative search engine."""
    if "www.bing.com/search" in url:
        query_params = urllib.parse.parse_qs(urllib.parse.urlparse(url).query)

        if "q" in query_params:
            search_query = query_params["q"][0]
            new_url = search_engine_url + urllib.parse.quote_plus(search_query).replace("%22", "")
            logging.info(f"Redirecting Bing search to: {new_url}")
            return new_url

    return url

def should_open_url(url, recent_urls):
    """Avoid opening the same URL twice in quick succession."""
    if url in recent_urls:
        logging.info(f"Skipping duplicate URL: {url}")
        return False
    recent_urls.append(url)
    if len(recent_urls) > 20:
        recent_urls.pop(0)
    return True

def close_edge_window(hwnd):
    """Closes the specified Edge window."""
    try:
        logging.info(f"Closing Edge window: {hwnd}")
        win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
    except Exception as e:
        logging.error(f"Failed to close Edge window: {e}")

def exit_action(icon, item):
    """Handles the 'Exit' menu item in the system tray."""
    # Clean up jiggler resources
    Jiggler.cleanup()
    
    logging.info("Exiting application via system tray.")
    icon.stop()
    os._exit(0)

def create_icon(icon_path):
    """Creates an Image object for the system tray icon."""
    try:
        return Image.open(icon_path)
    except Exception as e:
        logging.error(f"Failed to load icon: {e}")
        return Image.new('RGBA', (64, 64), (0, 0, 0, 0))

def open_log_file(icon, _):
    """Opens the log file with the default text editor."""
    try:
        # Get the log file path from the logger
        log_file = logging.getLogger().handlers[0].baseFilename
        
        # Check if the file exists
        if os.path.exists(log_file):
            logging.info(f"Opening log file: {log_file}")
            os.startfile(log_file)
        else:
            logging.error(f"Log file not found: {log_file}")
    except Exception as e:
        logging.error(f"Failed to open log file: {e}")
        
    # No need to update menu here since we're not changing state

def open_config_file(icon, _):
    """Opens the config.ini file with the default text editor."""
    try:
        # Try to get the user config path
        try:
            # Try relative import (when imported as a package)
            from .config import get_config_file_path
        except ImportError:
            # Fallback for direct script execution
            try:
                import config
                get_config_file_path = config.get_config_file_path
            except ImportError:
                get_config_file_path = None
                
        if get_config_file_path:
            config_file = get_config_file_path()
        else:
            # Fallback to direct path
            config_file = os.path.join(os.path.expanduser("~"), '.config', 'edger', 'config.ini')
            if not os.path.exists(config_file):
                config_file = "config.ini"
        
        # Ensure the directory exists
        config_dir = os.path.dirname(config_file)
        if not os.path.exists(config_dir):
            os.makedirs(config_dir, exist_ok=True)
        
        # If the file doesn't exist, try to copy from package or create empty
        if not os.path.exists(config_file):
            try:
                import pkg_resources
                default_config = pkg_resources.resource_filename('edger', 'config.ini')
                if os.path.exists(default_config):
                    import shutil
                    shutil.copy2(default_config, config_file)
                    print(f"Copied default configuration to: {config_file}")
            except (ImportError, pkg_resources.DistributionNotFound):
                # Create simple config if nothing else works
                with open(config_file, 'w') as f:
                    f.write("[Settings]\nsearch_engine_url = https://duckduckgo.com/?q=\n")
                    
        # Open the config file
        os.startfile(config_file)
        print(f"Opened config file: {config_file}")
    except Exception as e:
        print(f"Error opening config file: {e}")