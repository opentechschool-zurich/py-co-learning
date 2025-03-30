# Introduction to Python: Draw Flags with Turtle

This is a "fast" introduction to Python for people who cannot program but have already seen code (Scratch, ...)

## Why Python?

The only programming language that is used in production for almost all types of programming and has been created with the explicit goal to be easy to read and learn.

## What do Flags drawn by code look like?

Show the Swiss and South African Flags being drawn by Turtle.

![Switzerland](assets/ch.gif)

![Argentina](assets/ag.gif)

![Sourth Africa](assets/za.gif)

## Setup the environment

Install Mu-Editor: https://codewith.mu

## First steps in the REPL

Do a few simple variable exercises in the Mu-Editor's REPL  

- Press on the "REPL" button in the top toolbar
- In the panel displayed in the lower part of the window, after `In [1]:` type `print('Hello Python!')` and press the _Enter_ key
- Now type `3 + 2` and press again _Enter_.  
  The result (`5`) should be displayed.  
  Now:
  - You can try out calculation with the other operators (`+`, `-`, `*`, `/`)
  - Remarks:
    - You might see that we're adding spaces around the operator (`+`): Python understands your code even if you don't add those spaces, but for humans they really help to better read the code.  
      Some programming language leave much freedom to the programmers, and let them write in very different styles. On the contrary, the Python community enforces strict rules that make the code written by different people very similar (and easier to read by others and by your future self)
    - If the calculation gets complex, and if it mixes `+`, `-`, `*`, and `/`, then it might be worth to add parentheses to make the precedence explicit.
- Use some variables in the REPL:  
  ```py
    a = 4 <Type Enter>
    a <Enter>
    b <Enter>
    b = 2 <Enter>
    b <Enter>
    a * b <Enter>
    a + a - b <Enter>
  ```
  What is the result?
- Modify the variables in the REPL:  
  ```py
  b = 10 <Enter>
  a + b <Enter>
  ```

## Your first Program

In the main window, remove the text `# Write your code here :-)` and replace with:

```py
from turtle import *

forward(100)
```

You can press on the "Run" botton in the top toolbar to execute it (If you have not done so yet, Mu-Editor will ask you to save your code before running it for the first time; then, it will save it automatically each time you run it).

The program imports the `turtle` module and draws a line in the middle of the screen.

You can now continue your program.  
Here a few more `turtle` commands (you should probably type each command and not copy paste them; when you have typed a few of them, you can run the code and see what happens (and fix errors if any).

```py
from turtle import *

forward(100)
right(120)
forward(200)
left(120)
forward(100)
penup()
left(90)
forward(80)
right(90)
backward(20)
pendown()
backward(60)
penup()
forward(200)
```

This should draw a _Z_ on your screen.

One last thing: use a different thickness and color for the last line in the Z and add this code before that line is drawn:

```py
pencolor('blue')
pensize(8)
```

Make a small break and think of a (rather simple flag) that you want to draw with Turtle.

## Drawing a Flag with Turtle

- Decide which flag you want to draw (think of the lines and shapes you have drawn above and what you can draw with them.
- Rectangles are easy to draw:  
  ```py
  fillcolor('red')
  begin_fill()
  forward(100)
  left(90)
  forward(200)
  left(90)
  forward(100)
  left(90)
  forward(200)
  end_fill()
  ```
- Draw the flag on paper, if possible with the correct colors.  
  What shapes does it contain?
- Create a new file in Mu-Editor.
- Use the forward and `righ()` / `left()` commands to draw the outline of the shapes.
- Set the color of the outline for the different parts of the shapes
- Is it possible to simplify part of it with loops?  
  ```py
  for i in range(4):
     ...
  ```
- You probably need to define different colors for each cycle in the loop.  
  Add a list of colors before the for loop:  
  ```py
  colors = ['red', 'white', 'blue']
  ```
  You don't apply the color by its value but by the index in the `colors` list:  
  ```py
  fillcolor(colors[i])
  ```
  Where `i` is the variable that is filled by the `for` loop with the values from `0` to `3` (yes, in programming we start counting at 0: the first item in the list, `'red'`, is at the place `0`, and `'white'` at place `1`).
- Add the commands for starting and ending the filling of the shapes
- Add a comment before important parts of your code (a comment is a line that starts with `#` and which describes or explains the code).  
  You will probably have a comment saying:  
  ```py
  # Draw a colored rectangle
  ```
- If you have code that needs a description, it might be worth to move the code into a function, named in a very similar way as what you wrote in the comment:  
  ```py
  def draw_colored_rectangle(i):
      ...
  ```
  Create such a function, define its name and put the code in place of the three dots above.  
  The `i` is for passing the index of the color in the colors list
- Finally, you can improve the `draw_colored_rectangle()` function and give it good arguments:

  - the name of the color instead of its index
  - the width of the rectangle
  - the height of the rectangle

  At the end the function will have a signature similar to:  
  ```py
  def draw_colored_rectangle(color, width, height):
  ```
  and its call will be close to:  
  ```py
  draw_colored_rectangle(colors[i], 100, 150):
  ```


## Learning Python

- [Python Module beim CoderDojo Linz](https://linz.coderdojo.net/uebungsanleitungen/programmieren/python/)
- [Python 3 Tutorial](https://www.python-kurs.eu/python_kurs.php)
- [Das Python-Tutorial](https://py-tutorial-de.readthedocs.io/de/python-3.3/)

## Resources

- https://linz.coderdojo.net/uebungsanleitungen/programmieren/python/erste-schritte/
