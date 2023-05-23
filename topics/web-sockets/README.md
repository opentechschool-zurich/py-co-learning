# Websockets: a multiplayer four connect game

The WebSockets Python library suggests the [Four Connect game](https://websockets.readthedocs.io/en/stable/intro/tutorial1.html) tutorial as a good introduction to WebSockets.

## Running the code

Run a _backend_ server that provides the websockets:

```
python main.py
```

Run a _frontend_ server that serves the _public_ files through http:

```
cd public
python -m http.server
```
