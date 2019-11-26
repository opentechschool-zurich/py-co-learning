word = 'this_is_the_word'

output = ''
last_was_underscore = False
for c in word:
    if c == '_':
        last_was_underscore = True
    elif last_was_underscore:
        output += c.upper()
        last_was_underscore = False
    else:
        output += c
print(output)
