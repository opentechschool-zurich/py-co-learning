# Python Pip and venv

Python comes with batteries included. This means that lot of features are _automatically_ provided with it, that they are in the _standard library_.  
There is a lot  of functionalities that you can _activate_ with a simple `import` at the top of the file.

But when you start to work on a _real_ project you notice soon that there are packages that make your life easier when working on some parts of your code.  
Some examples are:

- Requests, for getting things out of the internet.
- PyGame, for creating games.
- Pillow, for manipulation images.
- NumPy, for powerful array operations and numerical computation.
- Pandas, for working with structured and time series data.
- Matplotlib, for data visualization.
- BeautifulSoup, for scraping information from web pages.


## Pip

Pip is the official package installer for Python.

It's basic usage is pretty simple:

```sh
pip install chardet
```

This will install _chardet_, a tool and library for detecting the character encoding of a file (ascii, utf-8, ...).


it will be installed _somewhere_ on your system.

You can find the location with:

```sh
pip show chardet
```

Typically, you should be then be able to use the library from your Python code:

```py
 import urllib.request
import chardet
rawdata = urllib.request.urlopen('http://yahoo.co.jp/').read()
print(chardet.detect(rawdata))
```

If you want to remove the package it's _simply_:

```sh
pip uninstall chardet
```

Since _chardet_ has no dependencies, this will go pretty well.  
But one big limitation of _pip_ is that it cannot remove the dependencies with the package that installed them.

Another big issue, is that, often the packages you install (or the code you write) will have specific requirements on the versions of the libraries it uses (oldest and newest ones it supports): if you use _pip_ often, at some time, you will get into conflicts.

## venv

Venv is a tool for creating "virtual environments", each with their own independent set of Python packages.

```sh
python -m venv venv
source venv/bin/activate
```

The files 

```sh
ls venv/lib64/python3.12/site-packages/
```

but if you look into `venv/bin` you will also find:

```sh
venv/bin/chardetect
```

Yes, pip also installed a tool that you can use on the command line!

## Figuring out what you have installed

If you want a list of all the packages you have installed for your project there is:

```sh
pip freeze > requirements.txt
```

This will fill the `requirements.txt` file with the list of all the packages you have installed and their respective version.

If you put this file at the route of your project, the people using your code (including your future self) will be able to recreate the full environment by doing:

```sh
pip install -r requirements.txt
```

Indeed, naming this file `requirements.txt` is pretty popular and you will find it in most repositories with Python code.

## Alternatives

What we have learned here, are the basics for managing 

- `conda`: The Anaconda package manager (that manages more than libraries)
- `pypenv`: Python Dev Workflow for Humans
- `poetry`: PYTHON PACKAGING AND DEPENDENCY MANAGEMENT MADE EASY (it's in all caps, so it must be true!)

The Zen of Python says:

    There should be one-- and preferably only one - obvious way to do it.

We see that we have here multiple solutions: each of them has drawbacks and advantages and no perfect tool seems to be existing yet.  
Pick one, the one you prefer and enjoy it!
