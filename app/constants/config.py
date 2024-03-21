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
    "settings": {"open_mode": "hold", "delay_min": "20", "delay_max": "50"},
}

settings_description = {
    "up": "Up",
    "down": "Down",
    "left": "Left",
    "right": "Right",
    "open": "Open stratagem menu",
    "open_mode": "Open mode (Hold/Toggle)",
    "delay_min": "Minimum delay",
    "delay_max": "Maximum delay",
}

settings_prompts = {
    "open_mode": "Do you want to use HOLD or TOGGLE mode for the stratagem open key? (h/t)",
    "delay_min": "Enter the minimum delay (ms)",
    "delay_max": "Enter the maximum delay (ms)",
    "open_mode_retry": "Invalid input. Please enter 'h' for HOLD or 't' for TOGGLE",
    "delay_retry": "The delay can't be empty"
}
