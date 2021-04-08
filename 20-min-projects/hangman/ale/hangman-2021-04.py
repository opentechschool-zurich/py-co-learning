# word = 'flower'
# solution = ['_'] * len(word)
# 
# def guess(char, word, solution):
#     return solution
# 
# solution = guess('o', word, solution)
# 
# print(''.join(solution))

# ------

# word = 'flower'
# solution = ['_'] * len(word)
# 
# def guess(char, word, solution):
#     for i, c in enumerate(word):
#         if char == c:
#             solution[i] = c
#     return solution
# 
# solution = guess('o', word, solution)
# print(''.join(solution))
# solution = guess('w', word, solution)
# print(''.join(solution))

# ------

# word = 'flower'
# solution = ['_'] * len(word)
# 
# lives = 5
# missing = solution.count('_')
# 
# def guess(char, word, solution):
#     for i, c in enumerate(word):
#         if char == c:
#             solution[i] = c
#     return solution
# 
# while lives > 0 and missing > 0:
#     print(''.join(solution), end='')
#     char = input(' ? ')
#     solution = guess(char, word, solution)
#     if missing == solution.count('_'):
#         lives -= 1
#     missing = solution.count('_')
# 
# print(word)
# if missing == 0:
#     print('you won')
# else:
#     print('you lost')

# ------

import urllib.request
import json
import string
import random
# get a random word from a random wikipedia article
# https://en.wikipedia.org/wiki/Special:Random
# https://en.wikipedia.org/w/api.php?action=query&format=json&titles=Bla_Bla_Bla&prop=extracts&exintro&explaintext
# https://en.wikipedia.org/w/api.php?format=json&action=query&generator=random&grnnamespace=0&prop=extracts&exintro&explaintext
with urllib.request.urlopen('https://en.wikipedia.org/w/api.php?format=json&action=query&generator=random&grnnamespace=0&prop=extracts&exintro&explaintext') as url:
    data = json.loads(url.read().decode())
    word = random.choice([w for w in list(data['query']['pages'].values())[0]['extract'].replace('\n', ' ').translate(str.maketrans('', '', string.punctuation)).translate(str.maketrans('', '', string.digits)).lower().split() if len(w) > 4])

# print(word)

solution = ['_'] * len(word)
hangman = [
  [' |--|',
   ' o  |',
   '-|- |',
   '/ \\ |',
   '    |'],
  [' |--|',
   ' o  |',
   '-|- |',
   '/   |',
   '    |'],
  [' |--|',
   ' o  |',
   '-|- |',
   '    |',
   '    |'],
  [' |--|',
   ' o  |',
   '-|  |',
   '    |',
   '    |'],
  [' |--|',
   ' o  |',
   ' |  |',
   '    |',
   '    |'],
  [' |--|',
   ' o  |',
   '    |',
   '    |',
   '    |'],
  [' |--|',
   '    |',
   '    |',
   '    |',
   '    |'],
  ['  --|',
   '    |',
   '    |',
   '    |',
   '    |'],
  ['    |',
   '    |',
   '    |',
   '    |',
   '    |'],
  ['     ',
   '     ',
   '     ',
   '     ',
   '     '],
]

lives = len(hangman) - 1
missing = solution.count('_')

def guess(char, word, solution):
    for i, c in enumerate(word):
        if char == c:
            solution[i] = c
    return solution

while lives > 0 and missing > 0:
    print()
    print('\n'.join(hangman[lives]))
    print(''.join(solution), end='')
    char = input(' ? ')
    solution = guess(char, word, solution)
    if missing == solution.count('_'):
        lives -= 1
    missing = solution.count('_')

print()
print('\n'.join(hangman[lives]))
print(word)
if missing == 0:
    print('you won')
else:
    print('you lost')
