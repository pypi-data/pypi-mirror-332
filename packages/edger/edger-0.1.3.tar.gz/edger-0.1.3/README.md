# Edger

<div align="center">

![Edger Logo](edger.ico)

*Reclaim your browser choice by redirecting Microsoft Edge to your default browser*

</div>

---

## 📋 Overview

**Edger** is a lightweight Windows utility that runs in your system tray and automatically redirects Microsoft Edge browser windows to your default browser. It's designed for users who prefer their browser of choice but find Edge being forced upon them in various contexts.

### Key Features

- 🔄 **Transparent Redirection**: Intercepts and redirects Edge windows to your default browser
- 🔍 **Bing Search Conversion**: Converts Bing searches to your preferred search engine
- 🛡️ **URL Bypass System**: Special handling for Microsoft Teams and other specified URLs
- 🔔 **System Tray Integration**: Easy toggle and access from your taskbar
- 📝 **Activity Logging**: Keeps records of redirects for troubleshooting
- 🖱️ **Mouse Jiggler**: Built-in invisible mouse activity simulator to prevent screen locking

---

## 🚀 Installation

### Prerequisites

- Windows Operating System
- Python 3.6 or higher
- Microsoft Edge browser installed

### Setup

1. **Clone or download** this repository
   ```
   git clone https://github.com/yourusername/edger.git
   cd edger
   ```

2. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```

3. **Configure** your preferences (optional)
   ```
   # Edit config.ini to customize behavior
   ```

4. **Run the application**
   ```
   python edger.py
   ```

---

## ⚙️ Configuration

Edger is configurable through the `config.ini` file:

```ini
[Settings]
search_engine_url = https://duckduckgo.com/?q=  # Your preferred search engine
log_file = edger.log                            # Log file location
icon_path = edger.ico                           # Path to system tray icon
jiggler_interval = 30                           # Seconds between mouse jiggle actions
detection_interval = 1                          # Seconds between checks for new Edge windows
default_jiggle = off                            # Start with jiggler enabled (on/off)
default_redirect = on                           # Start with redirection enabled (on/off)

[Bypass]
urls = statics.teams.cdn.office.net, example.com/redirect  # URLs to ignore
```

### Options Explained

| Setting | Purpose |
|---------|---------|
| `search_engine_url` | The search engine that replaces Bing (with query parameter) |
| `log_file` | Location for storing redirect logs |
| `icon_path` | Custom icon for the system tray |
| `jiggler_interval` | How often (in seconds) the mouse jiggler simulates activity |
| `detection_interval` | How often (in seconds) Edger checks for new Edge windows |
| `default_jiggle` | Whether the mouse jiggler is enabled at startup (on/off) |
| `default_redirect` | Whether Edge redirection is enabled at startup (on/off) |
| `urls` (in Bypass) | Comma-separated list of URLs that should not be redirected |

> **Note:** The bypass list is especially important for Microsoft Teams URLs which require special handling to work correctly.

---

## 🔧 Usage

Once running, Edger sits in your system tray (notification area) and works automatically:

1. When Edge opens, Edger captures the URL
2. The URL is processed (converted if it's a Bing search)
3. Your default browser opens with the same/converted URL
4. The Edge window is closed
5. The activity is logged for reference

### System Tray Controls

- **Left-click**: Access the menu
- **Redirect Edge Windows**: Toggle Edge redirection on or off
- **Mouse Jiggler**: Toggle the invisible mouse activity simulator
- **Settings**: Open the settings GUI to adjust intervals and default states
- **View Log**: Open the log file in your default text editor
- **Edit Config**: Open the config.ini file directly in your text editor
- **Exit**: Close the application

### Settings GUI

Edger includes a graphical settings panel accessible from the system tray menu. This allows you to easily configure:

- **Mouse Jiggle Interval**: How often (in seconds) the mouse jiggler simulates activity
- **Edge Detection Interval**: How often (in seconds) Edger checks for new Edge windows
- **Default States**: Whether features are enabled by default at startup

Changes made through the Settings GUI are saved to the config.ini file and applied immediately.

### Mouse Jiggler

The built-in mouse jiggler simulates mouse activity without actually moving your cursor. This prevents your computer from:
- Going to sleep
- Activating the screen saver
- Showing as "Away" or "Inactive" in messaging apps
- Triggering automatic locks

The jiggler is completely invisible - your cursor won't move on screen, but Windows will detect "activity".

---

## 📦 Dependencies

- **pystray**: System tray functionality
- **Pillow**: Image processing for the tray icon
- **pywin32**: Windows API integration
- **psutil**: Process monitoring
- **pyautogui**: GUI automation
- **pyperclip**: Clipboard management
- **configparser**: Configuration file handling

---

## ⚠️ Limitations

- Windows-only functionality
- May require updates if Edge's URL handling changes
- Not designed to bypass security measures
- Some URLs may need to be added to the bypass list

---

## 📄 License

[Add your license here]

---

<div align="center">
<p>Made with ❤️ for those who value browser choice</p>
</div> 