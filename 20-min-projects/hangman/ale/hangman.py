word = input('the word : ')
found = ''
errors = 0

while errors < 4:
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
        errors += 1
else:
    print('you\'ve lost')
