from pynput.keyboard import Key, Listener

def on_press_action(key):
    print('{0} pressed'.format(
        key))

def on_release_action(key):
    print('{0} release'.format(
        key))
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(
        on_press=on_press_action,
        on_release=on_release_action) as listener:
    listener.join()
