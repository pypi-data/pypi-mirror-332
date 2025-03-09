import ctypes
from ctypes import wintypes
import logging

# Jiggler state
jiggling_active = False
jiggler_interval = 30  # Default value, will be overridden by config
jiggler_counter = 0  # Counter to track when to jiggle

# Reference to the update menu function
update_menu_function = None

def set_menu_updater(update_func):
    """Sets the reference to the menu update function."""
    global update_menu_function
    update_menu_function = update_func

def set_interval(interval):
    """Sets the interval for the mouse jiggler."""
    global jiggler_interval
    jiggler_interval = interval
    logging.info(f"Jiggler interval set to {interval} seconds")

def jiggle_mouse_invisible():
    """Simulates mouse movement without actually moving the cursor."""
    # Define necessary constants
    MOUSEEVENTF_MOVE = 0x0001
    INPUT_MOUSE = 0
    
    class MOUSEINPUT(ctypes.Structure):
        _fields_ = [("dx", wintypes.LONG),
                   ("dy", wintypes.LONG),
                   ("mouseData", wintypes.DWORD),
                   ("dwFlags", wintypes.DWORD),
                   ("time", wintypes.DWORD),
                   ("dwExtraInfo", ctypes.POINTER(wintypes.ULONG))]
    
    class INPUT(ctypes.Structure):
        _fields_ = [("type", wintypes.DWORD),
                   ("mi", MOUSEINPUT)]
    
    # Create an INPUT structure with zero movement
    x = INPUT()
    x.type = INPUT_MOUSE
    x.mi = MOUSEINPUT()
    x.mi.dx = 0
    x.mi.dy = 0
    x.mi.dwFlags = MOUSEEVENTF_MOVE
    
    # Send the input event to reset idle timer
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))
    logging.debug("Mouse jiggled")

def process_jiggler(detection_interval):
    """Process the jiggler based on current state and intervals."""
    global jiggling_active, jiggler_interval, jiggler_counter
    
    if not jiggling_active:
        jiggler_counter = 0
        return
    
    # Increment counter by the detection interval
    jiggler_counter += detection_interval
    
    # Check if it's time to jiggle
    if jiggler_counter >= jiggler_interval:
        jiggle_mouse_invisible()
        jiggler_counter = 0  # Reset counter

def toggle(icon, _):
    """Toggle the mouse jiggler on and off."""
    global jiggling_active, jiggler_counter
    
    jiggling_active = not jiggling_active
    jiggler_counter = 0  # Reset counter on toggle
    
    if jiggling_active:
        logging.info("Mouse jiggler activated")
    else:
        logging.info("Mouse jiggler deactivated")
    
    # Use the update menu function
    if update_menu_function:
        update_menu_function()

def get_menu_text():
    """Get the menu text for the jiggler based on current state."""
    return f"Mouse Jiggler: {'ON' if jiggling_active else 'OFF'}"

def set_state(enabled):
    """Sets the initial state of the jiggler."""
    global jiggling_active
    
    # Only take action if we're changing state
    if enabled != jiggling_active:
        jiggling_active = enabled
        
        if jiggling_active:
            logging.info("Mouse jiggler activated (from config)")
    
    return jiggling_active

def cleanup():
    """Clean up jiggler resources."""
    global jiggling_active
    jiggling_active = False
    logging.info("Jiggler resources cleaned up")

def is_active():
    """Check if the jiggler is currently active."""
    global jiggling_active
    return jiggling_active
