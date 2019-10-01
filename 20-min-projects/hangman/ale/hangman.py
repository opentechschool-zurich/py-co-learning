word = input('the word : ')
found = ''
lifes = 4

while lifes > 0:
    output = ''.join([letter if letter in found else '-'
                      for letter in word])
    print(output)
    if output == word:
        print('you won')
        break
    guess = input('your guess: ')
    if guess in word:
        found += guess
    else:
        lifes -= 1
else:
    print('you\'ve lost')
