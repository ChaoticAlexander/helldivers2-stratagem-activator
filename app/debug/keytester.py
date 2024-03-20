import keyboard

arrow_key_names = ['up', 'down', 'left', 'right']
# 
def on_key_pressed(event):
  if event.event_type == keyboard.KEY_DOWN:
    print("Pressed key:", event.name, "\tDIK Code:", event.scan_code)
    is_arrow_key  = event.name in arrow_key_names
    
    extension = (event.is_keypad ^ is_arrow_key) or "right " in event.name
    print(f'key {'IS' if extension else 'IS NOT'} extended')
    print(event.__dict__)


print("Press any key. Press 'q' to quit.")
keyboard.hook(on_key_pressed)

# Keep the script running until 'q' is pressed.
while True:
  if keyboard.is_pressed('q'):
    break

keyboard.unhook_all()
