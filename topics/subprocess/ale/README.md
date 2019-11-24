# Getting output from a long running subprocess

- Run a long running subprocess.
- Get the output as soon as it is produced.
- Quit on a key press.

Notes:

- The output polling is a clean solution 
  - [Stackoverflow answer to "Constantly print Subprocess output while process is running"](https://stackoverflow.com/a/4417735/5239250)
- Polling for the keyboard press is the best i could find but needs a bit too much setup and teardown.
  - [Stackoverflow answer to "What's the simplest way of detecting keyboard input in python from the terminal?"](https://stackoverflow.com/a/13207724/5239250) (it's the second solution in the list)
  - It probably only works on Linux.
  - I've created a [self-cleaning object](https://stackoverflow.com/a/865272/5239250) around it.
  - An alternative approach could be [with a decorator](https://docs.python.org/3/library/contextlib.html#contextlib.contextmanager).

    ```py
import contextlib


class Resource:
    def __init__(self, dependency):
        self.dep = dependency

    @contextlib.contextmanager
    @classmethod
    def ctx(cls, dependency):
        prepare()
        yield cls(dependency)
        cleanup()

with Resource.ctx('some dep') as res:
    res.do_stuff()
    ```

	[Sample code by cdunklau](https://gist.github.com/cdunklau/eb6f11efe3e5af5c29a592cbe373a3ea)

    - alternative approaches for returning all the key strokes in the _cache_:
      - using the walrus operator:

        ```py
        while c := sys.stdin.read(1):
            yield c
        ```

      - a one-liner:

        ```py
        return list(iter(lambda: sys.stdin.read(1), ""))
        ```

        where "" is a sentinel that stops the iterator.

  - I've tried the `keyboard` module needs root on Linux.
  - I've tried the `pynput` but:
    - captures esc, but not a...
    - does not (cleanly) suppress the characters from the terminal output
- And now we have to solve the fact that `readline()` is blocking
  - <https://stackoverflow.com/questions/375427/non-blocking-read-on-a-subprocess-pipe-in-python>
