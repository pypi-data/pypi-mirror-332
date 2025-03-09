#!/usr/bin/env python

import webbrowser
import pystray
import config as Config
import utils as Utils
import log as Logging
import jiggler as Jiggler  # Capitalize the module alias for consistency
import config_gui  # Import the new config GUI module

import logging
import time
from PIL import Image
import os
import tkinter as tk
import threading
import pkg_resources
import shutil
import sys
import importlib.util

# Global state
running = True
# Global icon reference for external modules to use
system_tray_icon = None

# Setup module imports based on how we're being run
def setup_imports():
    """Set up imports based on execution context."""
    # Import necessary modules dynamically
    global Config, Log, Utils, Jiggler
    
    # Check if we're being imported as part of a package
    try:
        from . import config as Config
        from . import log as Log
        from . import utils as Utils 
        from . import jiggler as Jiggler
        return True  # Success with relative imports
    except ImportError:
        # Not in a package, try direct imports
        try:
            import config as Config
            import log as Log
            import utils as Utils
            import jiggler as Jiggler
            return True  # Success with direct imports
        except ImportError:
            # Last resort - try to find modules in the same directory
            module_dir = os.path.dirname(os.path.abspath(__file__))
            if module_dir not in sys.path:
                sys.path.insert(0, module_dir)
            try:
                import config as Config
                import log as Log
                import utils as Utils
                import jiggler as Jiggler
                return True  # Success with path-adjusted imports
            except ImportError:
                print("ERROR: Could not import required modules!")
                return False

# Run setup immediately
if not setup_imports():
    print("Failed to import required modules. Exiting.")
    sys.exit(1)

# Lazy import for config_gui to avoid circular imports
config_gui = None

def get_running_text():
    """Get the menu text for the edge redirect functionality."""
    return "Redirect Edge Windows"

def toggle_running(icon, item):
    """Toggle the global 'running' variable and update the menu."""
    global running
    running = not running
    print(f"Running is now set to {running}")
    # Update the menu with new text
    icon.menu = create_menu()
    # No need to call update_menu() as setting the menu property handles this

def reload_settings(current_running=None, current_jiggler=None):
    """Reload settings from config.ini.
    
    Args:
        current_running: If provided, updates the running state
        current_jiggler: If provided, updates the jiggler state
    """
    global running
    
    # Get the updated configuration
    config_values = Config.load_configuration()
    search_engine_url, log_file, bypass_list, icon_path, jiggler_interval, default_jiggle, default_redirect, detection_interval = config_values
    
    # Update jiggler settings
    Jiggler.set_interval(jiggler_interval)
    
    # Update current states if provided (from settings window)
    if current_running is not None:
        running = current_running
        logging.info(f"Updated running state from settings: {running}")
    
    if current_jiggler is not None:
        if current_jiggler and not Jiggler.is_active():
            Jiggler.start()
        elif not current_jiggler and Jiggler.is_active():
            Jiggler.stop()
        logging.info(f"Updated jiggler state from settings: {Jiggler.is_active()}")
    
    # Log the reload
    logging.info("Settings reloaded from config.ini")
    
    # Update the menu
    if system_tray_icon:
        system_tray_icon.menu = create_menu()

def open_settings():
    """Open the settings GUI with safety precautions for threading."""
    try:
        global running, config_gui
        # Log that we're attempting to open settings
        print("Opening settings window...")
        logging.info("Opening settings window")
        
        # Import here to avoid circular imports
        if config_gui is None:
            # Try relative import first
            try:
                from . import config_gui as config_gui_module
                config_gui = config_gui_module
            except ImportError:
                # Fallback to direct import
                import config_gui as config_gui_module
                config_gui = config_gui_module
        
        # Check for and remove any leftover temp files from previous attempts
        if os.path.exists("settings_updated.tmp"):
            os.remove("settings_updated.tmp")
        
        # Launch the settings window
        config_gui.open_settings_window(
            on_save_callback=reload_settings,
            running_state=running,
            jiggler_state=Jiggler.is_active()
        )
        
        # Set up a simple polling mechanism for the settings file
        def check_for_settings_file():
            if os.path.exists("settings_updated.tmp"):
                try:
                    with open("settings_updated.tmp", "r") as f:
                        data = f.read().strip().split(",")
                    
                    if len(data) == 2:
                        # Get the new states
                        new_running = data[0].lower() == "true"
                        new_jiggler = data[1].lower() == "true"
                        
                        # Apply changes directly 
                        reload_settings(new_running, new_jiggler)
                        
                        # Clean up
                        os.remove("settings_updated.tmp")
                    return
                except Exception as e:
                    logging.error(f"Error processing settings update: {e}")
        
        # Just check once after a short delay
        threading.Timer(0.5, check_for_settings_file).start()
            
    except Exception as e:
        error_msg = f"Error opening settings window: {e}"
        print(error_msg)
        logging.error(error_msg)
        import traceback
        logging.error(traceback.format_exc())

def create_menu():
    """Create the system tray menu with current state."""
    # Import necessary modules here to ensure the imports work when called later
    try:
        from . import utils as Utils
        from . import jiggler as Jiggler
    except ImportError:
        import utils as Utils
        import jiggler as Jiggler
    
    import pystray
    
    # Create the menu
    return pystray.Menu(
        # Toggle options
        pystray.MenuItem(
            get_running_text(),
            toggle_running,
            checked=lambda item: running
        ),
        pystray.MenuItem(
            "Mouse Jiggler",
            Jiggler.toggle,
            checked=lambda item: Jiggler.is_active()
        ),
        # Separator between toggle options and file operations
        pystray.Menu.SEPARATOR,
        # File operations
        pystray.MenuItem(
            "Settings",
            open_settings
        ),
        pystray.MenuItem(
            "View Log",
            Utils.open_log_file
        ),
        # Separator before exit
        pystray.Menu.SEPARATOR,
        pystray.MenuItem(
            "Exit",
            Utils.exit_action
        )
    )

def update_icon_menu():
    """Updates the system tray icon menu - can be called from external modules."""
    global system_tray_icon
    if system_tray_icon:
        system_tray_icon.menu = create_menu()

def detection_loop(search_engine_url, bypass_list, detection_interval):
    """Main detection loop."""
    known_windows = set()
    recent_urls = []
    print("Edger is running...")
    while running:
        # Process the jiggler (if active)
        Jiggler.process_jiggler(detection_interval)
        
        # Sleep for the configured interval
        time.sleep(detection_interval)
        
        # Edge window detection
        current_windows = set(Utils.get_edge_windows())
        new_windows = current_windows - known_windows
        for hwnd in new_windows:
            logging.info(f"New Edge window detected (HWND: {hwnd})")
            url = Utils.get_edge_url(hwnd, bypass_list)
            if url:
                new_url = Utils.convert_bing_to_alternative(url, search_engine_url)
                if Utils.should_open_url(new_url, recent_urls):
                    logging.info(f"Opening URL in default browser: {new_url}")
                    webbrowser.open(new_url)
                    if not any(bypass_url in url for bypass_url in bypass_list):
                        Logging.log_redirect(url, new_url, bypass_list)
                Utils.close_edge_window(hwnd)
        known_windows = current_windows

def run_with_system_tray(search_engine_url, bypass_list, icon_file, detection_interval):
    """Runs the main loop within the system tray context."""
    global running, system_tray_icon
    running = True
    image = Utils.create_icon(icon_file)
    
    # Create the icon with a dynamic menu - using standard pystray.Icon now
    system_tray_icon = pystray.Icon("Edge Redirect", image, "Edge Redirect")
    system_tray_icon.menu = create_menu()
    
    # Make the icon available to Utils
    Utils.set_system_tray_icon(update_icon_menu)
    
    # Run the icon in a separate thread
    system_tray_icon.run_detached()
    
    # Start the main detection loop
    detection_loop(search_engine_url, bypass_list, detection_interval)

def initialize_user_config():
    """Initialize user configuration directory and files if they don't exist."""
    import shutil
    
    # Get config and icon path functions
    try:
        # Try relative import first for package use
        from .config import get_config_file_path, get_icon_path
    except ImportError:
        # Fallback to normal import for direct script execution
        try:
            from config import get_config_file_path, get_icon_path
        except ImportError:
            # Create simple functions as a last resort
            def get_config_file_path():
                return os.path.join(os.path.expanduser("~"), '.config', 'edger', 'config.ini')
            
            def get_icon_path():
                return os.path.join(os.path.expanduser("~"), '.config', 'edger', 'edger.ico')
    
    # Create user config directory
    user_config_dir = os.path.join(os.path.expanduser("~"), '.config', 'edger')
    if not os.path.exists(user_config_dir):
        os.makedirs(user_config_dir, exist_ok=True)
        print(f"Created user configuration directory: {user_config_dir}")
    
    # Check if user config file exists, if not copy the default one
    user_config_file = os.path.join(user_config_dir, 'config.ini')
    if not os.path.exists(user_config_file):
        # Try to find the package default config
        try:
            default_config = pkg_resources.resource_filename('edger', 'config.ini')
            if os.path.exists(default_config):
                shutil.copy2(default_config, user_config_file)
                print(f"Copied default configuration to: {user_config_file}")
        except (ImportError, pkg_resources.DistributionNotFound):
            # Fallback to local file
            local_config = os.path.join(os.path.dirname(__file__), 'config.ini')
            if os.path.exists(local_config):
                shutil.copy2(local_config, user_config_file)
                print(f"Copied default configuration to: {user_config_file}")
    
    # Check for icon file too
    user_icon_file = os.path.join(user_config_dir, 'edger.ico')
    if not os.path.exists(user_icon_file):
        try:
            default_icon = pkg_resources.resource_filename('edger', 'data/edger.ico')
            if os.path.exists(default_icon):
                shutil.copy2(default_icon, user_icon_file)
                print(f"Copied default icon to: {user_icon_file}")
        except (ImportError, pkg_resources.DistributionNotFound):
            # Fallback to local file
            local_icon = os.path.join(os.path.dirname(__file__), 'data', 'edger.ico')
            if os.path.exists(local_icon):
                shutil.copy2(local_icon, user_icon_file)
                print(f"Copied default icon to: {user_icon_file}")

def main():
    """Main entry point for the application."""
    # Initialize user configuration files
    initialize_user_config()
    
    # Get configuration values
    config_values = Config.load_configuration()
    search_engine_url, log_file, bypass_list, icon_path, jiggler_interval, default_jiggle, default_redirect, detection_interval = config_values
    
    # Set up logging
    Logging.configure_logging(log_file)
    
    # Start with default states from config
    global running
    running = default_redirect
    
    # Set jiggler interval and initial state
    Jiggler.set_interval(jiggler_interval)
    Jiggler.set_state(default_jiggle)
    
    # Run with system tray icon
    run_with_system_tray(search_engine_url, bypass_list, icon_path, detection_interval)

# Allow direct execution
if __name__ == "__main__":
    main()
