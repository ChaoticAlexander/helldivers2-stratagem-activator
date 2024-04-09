from app.types.config import AppConfig

config_file_path = "config.ini"

default_settings: AppConfig = {
    "keybindings": {
        "left": "75.1",
        "right": "77.1",
        "up": "72.1",
        "down": "80.1",
        "open": "29",
    },
    "settings": {"open_mode": "hold", "delay_min": "20", "delay_max": "50", "press_time": "40"},
}

settings_description = {
    "up": "Up",
    "down": "Down",
    "left": "Left",
    "right": "Right",
    "open": "Open stratagem menu",
    "open_mode": "Open mode (Hold/Toggle/None)",
    "delay_min": "Minimum delay between key presses (ms)",
    "delay_max": "Maximum delay between key presses (ms)",
    "press_time": "Time to hold a key down for (ms)",
}

settings_prompts = {
    "open_mode": "Do you want to use HOLD, TOGGLE or NONE mode for the stratagem open key? (h/t/n)",
    "delay_min": "Enter the minimum delay between key presses (ms)",
    "delay_max": "Enter the maximum delay between key presses (ms)",
    "press_time": "Enter the time to hold a key down for (ms)",
    "open_mode_retry": "Invalid input. Please enter 'h' for HOLD or 't' for TOGGLE"
}
