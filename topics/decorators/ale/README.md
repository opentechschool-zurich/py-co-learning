# Introduction to decorators

- `main-pynput.py`: standard usage of `pyinput`.
- the `on_press_action` and `on_release_action` functions process all keys and are my actions but:
  - have to manage all the keys
  - the relations ship with the `pynput` is not self explanatory.
  - at the end we need to pass all the actions to the pynput library
- `main-decorator.py`: the standard example from the documentation on how to create a decorator
- `main.py`: create a decorator to attach action to _key released_ events:
  - most of the code relating to the event loop can be hidden away in an external library
  - each _key release_ event can be invidually attached to an action.
  - the relationship is created through the decorator at the same place where the action is defined.

The code runs with `python3` and it needs `pip install pynput` (if possible in a venv...).
