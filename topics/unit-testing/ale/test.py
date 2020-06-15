from main import text_to_words

assert(text_to_words('dies sind worte') == ['dies', 'sind', 'worte'])
assert(text_to_words('hier ist ein wort: sonne') == ['hier', 'ist', 'ein', 'wort', 'sonne'])
# assert(text_to_words('dies sind worte.') == ['dies', 'sind', 'worte',''])
