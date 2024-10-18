from pynput import keyboard

def on_press(key):
    try:
        print(f"Pressed key: {key.char}")
    except AttributeError:
        print(f"Special key pressed: {key}")

if __name__ == "__main__":
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()