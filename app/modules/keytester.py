import keyboard
import colorama
import shutil
from colorama import Fore, Style
from app.utils.config import filter_event


class Keytester:
    last_action = None

    def __init__(self):
        colorama.init()
        print("Press any key. Press 'esc' to quit.")
        self.print_separator()
        keyboard.hook(self.on_key_pressed)

        # Keep the script running until 'esc' is pressed.
        while True:
            if keyboard.is_pressed("esc"):
                keyboard.unhook_all()
                break

    def on_key_pressed(self, event):
        if event.event_type == self.last_action and event.event_type != keyboard.KEY_UP:
            self.print_separator()

        is_extended = filter_event(event)["is_extended"]
        style = Fore.GREEN if event.event_type == keyboard.KEY_DOWN else Fore.RED

        print(
            Style.RESET_ALL + style,
            "Pressed:" if event.event_type == keyboard.KEY_DOWN else "Released:",
            Style.RESET_ALL,
            f"{Fore.YELLOW}{event.name.upper()} -",
            (Fore.GREEN + "EXTENDED" if is_extended else Fore.RED + "NOT EXTENDED")
            + "\n",
            Style.RESET_ALL + Style.DIM,
            event.__dict__,
        )

        if event.event_type == keyboard.KEY_UP:
            self.print_separator()
        self.last_action = event.event_type

    def print_separator(self):
        print()
        print(Style.DIM, self.get_terminal_width() * "-")
        print()

    def get_terminal_width(self):
        try:
            terminal_size = shutil.get_terminal_size()
            return terminal_size.columns - 1
        except OSError:
            return 50
