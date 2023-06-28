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
        for w, s in zip(word, status):
            if w == guess:
                new_status += w
            else: 
                new_status += s
        status = new_status
        if status == word:
            break
    else:
        print('k.o.')
        failures += 1

