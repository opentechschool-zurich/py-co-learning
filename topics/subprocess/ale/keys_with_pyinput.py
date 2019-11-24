from pynput.keyboard import Key, Listener

def on_release(key):
    print('{0} release'.format(key))
    if key == Key.esc:
        # Stop listener
        return False
    if key == 'a':
        # Stop listener
        return False

with Listener(
        on_release=on_release) as listener:
    listener.join()
