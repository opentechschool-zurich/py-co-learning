failures = 0 # max is 6
word = 'Forest'
word = word.lower()
status = '_'* len(word)

while failures < 6:
    print(status)
    guess = input('Next guess: ')
    guess = guess[0].lower()
    if guess in word:
        new_status = ''
        for i, l in enumerate(word):
            if l == guess:
                new_status += guess
            else: 
                new_status += status[i]
        status = new_status
        if status == word:
            break
    else:
        print('k.o.')
        failures += 1

