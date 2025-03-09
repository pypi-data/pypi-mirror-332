import configparser
import os
import sys
import pkg_resources

def get_config_file_path():
    """
    Determine the appropriate config file path.
    Tries user's home directory first, then falls back to package config.
    """
    # First, check if there's a config file in the user's .config directory
    user_config = os.path.join(os.path.expanduser("~"), '.config', 'edger', 'config.ini')
    
    if os.path.exists(user_config):
        return user_config
    
    # Otherwise, check the current directory (useful for development)
    if os.path.exists("config.ini"):
        return "config.ini"
    
    # As a last resort, use the package's default config
    try:
        return pkg_resources.resource_filename('edger', 'config.ini')
    except (ImportError, pkg_resources.DistributionNotFound):
        # Fallback during development
        return os.path.join(os.path.dirname(__file__), "config.ini")

def get_icon_path():
    """Get the appropriate icon path."""
    # First check if there's a custom icon in the user's .config directory
    user_icon = os.path.join(os.path.expanduser("~"), '.config', 'edger', 'edger.ico')
    
    if os.path.exists(user_icon):
        return user_icon
    
    # Otherwise, check the current directory (useful for development)
    if os.path.exists("edger.ico"):
        return "edger.ico"
    
    # As a last resort, use the package's default icon
    try:
        return pkg_resources.resource_filename('edger', 'data/edger.ico')
    except (ImportError, pkg_resources.DistributionNotFound):
        # Fallback during development
        return os.path.join(os.path.dirname(__file__), "data", "edger.ico")

def load_configuration():
    """Loads configuration from config.ini file."""
    config = configparser.ConfigParser()
    config_file = get_config_file_path()

    if not os.path.exists(config_file):
        print(f"[ERROR] Missing config file: {config_file}")
        exit(1)

    config.read(config_file)
    search_engine_url = config.get("Settings", "search_engine_url", fallback="https://duckduckgo.com/?q=")
    log_file = config.get("Settings", "log_file", fallback="edge_redirects.log")
    icon_path = get_icon_path()  # Use our new icon path getter
    jiggler_interval = config.getint("Settings", "jiggler_interval", fallback=30)
    detection_interval = config.getfloat("Settings", "detection_interval", fallback=1.0)
    
    # Get default states (converting string to boolean)
    default_jiggle = config.get("Settings", "default_jiggle", fallback="off").lower() == "on"
    default_redirect = config.get("Settings", "default_redirect", fallback="on").lower() == "on"
    
    bypass_list = [url.strip() for url in config.get("Bypass", "urls", fallback="").split(",") if url.strip()]

    return search_engine_url, log_file, bypass_list, icon_path, jiggler_interval, default_jiggle, default_redirect, detection_interval