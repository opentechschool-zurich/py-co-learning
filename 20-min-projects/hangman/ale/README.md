# Hangman

This is my short and dense solution.

Steps towards a _simple_ solution:

1. Define a word and print each letter, one at a time.
2. Print an underscore (`_`) in place of each letter.
3. Read a character from `input()` and print each letter
   - as is, if it matches the input, or
   - or as a dash if it does not match.
4. Repeat multiple times
   - the input of the letter and
   - the output of letters and dashes.
5. Retain the letters from the previous inputs.
6. Stop if all letters have been found.
7. Stop if there were more than `n` errors.
8. Print if the user has won or lost.
