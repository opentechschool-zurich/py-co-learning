from pynput.keyboard import Key, Listener

### this is library code 

class Events:
    def __init__(self):
        self.events = {}
    def key_add(self, key):
        def decorator(f):
            self.events[key] = f
        return decorator

    def on_release(self, key):
        if key == Key.esc:
            # Stop listener
            return False
        elif key.char in self.events:
            self.events[key.char]()

events = Events()

### end of the library code 

@events.key_add('a')
def show_meteo():
    print('i will show the meteo')

@events.key_add('b')
def show_temperature():
    print('i will show the °C')


# start the event loop
with Listener(
        on_release=events.on_release) as listener:
    listener.join()

