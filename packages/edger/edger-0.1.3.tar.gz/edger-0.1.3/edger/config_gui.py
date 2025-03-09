import tkinter as tk
import configparser
import os
import sys
import threading

# Global variables to store results from the settings window
_save_result = None
_settings_values = None
_running_state = None
_jiggler_state = None

def open_settings_window(on_save_callback=None, running_state=None, jiggler_state=None, 
                        toggle_running=None, toggle_jiggler=None):
    """Opens the settings window in a more conservative way to avoid threading issues.
    
    This implementation avoids direct threading conflicts by isolating the Tkinter
    main loop better and using global variables for communication.
    """
    global _running_state, _jiggler_state
    
    # Store the current states
    _running_state = running_state
    _jiggler_state = jiggler_state
    
    # Run the actual window function in a separate thread
    threading.Thread(target=lambda: _create_settings_window(on_save_callback)).start()
    
def _create_settings_window(on_save_callback):
    """Implements the actual settings window."""
    global _running_state, _jiggler_state
    
    # Create a new window with popup-like properties
    root = tk.Tk()
    root.title("Edger Settings")
    root.geometry("290x270")
    root.minsize(290, 270)
    
    # Remove minimize and maximize buttons (Windows-specific)
    root.attributes('-toolwindow', True)  # Gives a dialog-style window
    
    # Make it act like a modal dialog
    root.grab_set()  # Grab all input events
    root.focus_force()  # Force focus to this window
    
    # Add icon if available - but suppress errors
    try:
        # First try to use the get_icon_path function from config module if available
        try:
            # Try relative import (when imported as a package)
            from .config import get_icon_path
        except ImportError:
            # Fallback for direct script execution
            try:
                import config
                get_icon_path = config.get_icon_path
            except ImportError:
                get_icon_path = None
                
        if get_icon_path:
            icon_path = get_icon_path()
            if os.path.exists(icon_path):
                root.iconbitmap(icon_path)
        else:
            # Fallback to direct path for compatibility
            if os.path.exists("edger.ico"):
                root.iconbitmap("edger.ico")
    except Exception:
        # Just silently ignore icon errors as they don't affect functionality
        pass
    
    # Load config
    try:
        # Try to import our config module
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
            config_file = "config.ini"
    except Exception:
        # Fallback to direct path
        config_file = "config.ini"
    
    config = configparser.ConfigParser()
    config.read(config_file)
    
    # Create variables - removed default state variables
    current_redirect = tk.IntVar(value=1 if _running_state else 0)
    current_jiggle = tk.IntVar(value=1 if _jiggler_state else 0)
    jiggler_interval = tk.IntVar(value=config.getint("Settings", "jiggler_interval", fallback=30))
    detection_interval = tk.DoubleVar(value=config.getfloat("Settings", "detection_interval", fallback=1.0))
    
    # Toggle functions
    def toggle_redirect():
        global _running_state
        _running_state = not _running_state
        current_redirect.set(1 if _running_state else 0)
        print(f"Settings: Redirect toggled to {_running_state}")
    
    def toggle_jiggler():
        global _jiggler_state
        _jiggler_state = not _jiggler_state
        current_jiggle.set(1 if _jiggler_state else 0)
        print(f"Settings: Jiggler toggled to {_jiggler_state}")
    
    # Save function - updated to remove default state settings
    def save_settings():
        global _running_state, _jiggler_state
        
        print("Saving settings...")
        # Update config - removed default state settings
        config["Settings"]["jiggler_interval"] = str(jiggler_interval.get())
        config["Settings"]["detection_interval"] = str(detection_interval.get())
        
        # Ensure user config directory exists
        user_config_dir = os.path.join(os.path.expanduser("~"), '.config', 'edger')
        if not os.path.exists(user_config_dir):
            os.makedirs(user_config_dir, exist_ok=True)
            print(f"Created user configuration directory: {user_config_dir}")
        
        # Always save to user config file
        user_config_file = os.path.join(user_config_dir, 'config.ini')
        
        # Save to file
        with open(user_config_file, "w") as configfile:
            config.write(configfile)
        
        # Store current states and signal success
        with open("settings_updated.tmp", "w") as f:
            f.write(f"{_running_state},{_jiggler_state}")
        
        print("Settings saved successfully")
        
        # Close the window safely
        root.quit()
        root.destroy()
    
    # Safe close function
    def on_close():
        print("Closing settings window...")
        root.quit()
        root.destroy()
    
    # Handle window close and escape key
    root.protocol("WM_DELETE_WINDOW", on_close)
    root.bind("<Escape>", lambda event: on_close())
    
    # Main container - use grid layout for more reliable positioning
    main_frame = tk.Frame(root, padx=20, pady=20)
    main_frame.pack(fill=tk.BOTH, expand=True)
    
    # Configure 2 rows in main frame
    main_frame.grid_rowconfigure(0, weight=1)  # Content area expands
    main_frame.grid_rowconfigure(1, weight=0)  # Button area fixed
    main_frame.grid_columnconfigure(0, weight=1)
    
    # Content frame for all settings
    content_frame = tk.Frame(main_frame)
    content_frame.grid(row=0, column=0, sticky="nsew")
    
    # Current States
    row = 0
    tk.Checkbutton(content_frame, text="Redirect Edge Windows", variable=current_redirect, command=toggle_redirect).grid(row=row, column=0, sticky="w", pady=2)
    row += 1
    tk.Checkbutton(content_frame, text="Enable Mouse Jiggler", variable=current_jiggle, command=toggle_jiggler).grid(row=row, column=0, sticky="w", pady=2)
    row += 1
    
    # Spacer
    tk.Frame(content_frame, height=10).grid(row=row, column=0)
    row += 1
    
    # Intervals
    jiggle_frame = tk.Frame(content_frame)
    jiggle_frame.grid(row=row, column=0, sticky="ew", pady=2)
    tk.Label(jiggle_frame, text="Mouse Jiggle Interval:").pack(side=tk.LEFT)
    tk.Spinbox(jiggle_frame, from_=1, to=300, width=5, textvariable=jiggler_interval).pack(side=tk.RIGHT)
    row += 1
    
    detect_frame = tk.Frame(content_frame)
    detect_frame.grid(row=row, column=0, sticky="ew", pady=2)
    tk.Label(detect_frame, text="Edge Detection Interval:").pack(side=tk.LEFT)
    tk.Spinbox(detect_frame, from_=0.1, to=10.0, increment=0.1, width=5, textvariable=detection_interval, format="%.1f").pack(side=tk.RIGHT)
    row += 1
    
    # Separator 
    separator = tk.Frame(content_frame, height=1, bg="gray")
    separator.grid(row=row, column=0, sticky="ew", pady=15)
    
    # Button area - fixed at bottom with left alignment
    button_frame = tk.Frame(main_frame)
    button_frame.grid(row=1, column=0, sticky="w", pady=10)
    
    # Left-aligned buttons
    # Cancel button
    cancel_btn = tk.Button(
        button_frame, 
        text="Cancel", 
        width=10,
        command=on_close
    )
    cancel_btn.pack(side=tk.LEFT, padx=5)
    
    # Save button
    save_btn = tk.Button(
        button_frame, 
        text="Save", 
        background="#4CAF50",
        foreground="white",
        width=10,
        command=save_settings
    )
    save_btn.pack(side=tk.LEFT, padx=5)
    
    # Position window at bottom right of screen
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    
    # Get screen dimensions
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    # Calculate position for bottom right (with some margin)
    x = screen_width - width - 20
    y = screen_height - height - 110  # Raised twice as far as before
    
    # Set position
    root.geometry(f"{width}x{height}+{x}+{y}")
    
    # Start main loop
    root.mainloop()

# For testing directly
if __name__ == "__main__":
    open_settings_window() 