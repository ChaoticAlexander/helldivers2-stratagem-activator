import keyboard


def on_key_pressed(event):
  if event.event_type == keyboard.KEY_DOWN:
    print("Pressed key:", event.name, "\tDIK Code:", event.scan_code)


print("Press any key. Press 'q' to quit.")
keyboard.hook(on_key_pressed)

# Keep the script running until 'q' is pressed.
while True:
  if keyboard.is_pressed('q'):
    break

keyboard.unhook_all()
