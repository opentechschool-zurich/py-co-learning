import re

def text_to_words(text):
    return re.split(' |: |\.',text)

def main():
    text = input('a few words:')
    print(text_to_words(text))


if __name__ == "__main__":
    main()
