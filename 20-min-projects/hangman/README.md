# The hangman

The user has to guess a word, letter by letter.

# Hangman

```
#     ----
#     0  |
#    /|\ |
#    / \ |
#        |
#    -----
#
#
# - There is a random word
# - The player wants to guess it
# - The player suggest a letter
# - If the letter is in the word it gets shown
# - Otherwise there is a penalty point (hangman)
# - Extra: take a random word from a random Wikipedia article
```

Programming the Hangman is a nice exercise, that can help you learn different topics about programming

You can start with learning how to check if a letter is in a word and counting the number of (failed) tries. It's a nice task for beginners.  
There is a lot to be learned: different data structures to store the word and the letters, ways of going through lists, ... and you will probably learn that it's not so easy to know, if the user has correctly guessed the word in a given number of tries.

There is a number of topics you can explore from there:

- Getting a random word
- Creating a GUI (ASCII, PyQt, TKinter, ...)
- Quering APIs to get random words from a random page (Wikipedia)
- Scarping Websites to get a random word (Newspaper...)

A possible way to approach the exercise:

- first have some code that checks if a letter is in a given word
- then pick a random word from a list
- then find out how to use the Wikipedia API (i can give you the link to the documentation if you don't find it)
- use the Python Requests package to make a request to any Wikipedia API call
- in the Wikipedia API documentation find out how to get a random page and, then how to get some raw text out of it
- In Python, filter the resulting text and keep words that are likely to be ok for the game ('the' is not : - )
- Ask the user for input in the terminal
- Create a GUI with TKinter or Qt
