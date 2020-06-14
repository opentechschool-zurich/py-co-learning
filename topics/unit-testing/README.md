# Unit testing

Testing that the parts of an application work correctly.

In other words: the public interfaces of the modules that compose the software work correctly.

The extreme way: TDD, Test Driven Development. You first build the tests, one at a time, then check that it fails and write the minimal code that makes the test pass. (Only when the "raw feature" has been added and all test passes, you are allowed to do software engineering work and refactor your code to _look good_)

The easy way: each time a bug is found, first write a test that replicates the bug, then fix the code.

There is much tooling and often a bit of magic aura around Unit Testin. But, if for real life examples, you should use a Testing Framework, for very simple script a bunch of asserts can help you focus on the ways to use testing for improving your program.

Questions:

<details><summary>Which problems are a better and / or worse fit for unit testing?</summary>

  - algorithm are easy
  - collecting data is hard

</details>

<details><summary>What is mocking?</summary>

  - database
  - reading files
  - data from the web

  You can provide "test" data or write code that returns _good_ answers.
</details>

## Examples

### Split a text in words

Starting code:

```py

def text_to_words(text):
    return []

def main():
    text = input('a few words:')
    print(text_to_words(text))

if __name__ == "__main__":
    main()
```

Steps:

- start with words separated by spaces: `today is a nice day`
- add a comma in the middle `today, is a rainy day`
- add a period at the end `today, is a rainy day.`
- add a few more separators: `today, is a rainy day: let's start with unit testing`
- multiline text:  
`today, is a rainy day:`  
`let's start with unit testing`

### Number and operators

You have a list of `n` numbers, find the operator that give a specific result:

```
1 ? 2 ? 3 ? 4 == 24
1 * 2 * 3 * 4 == 24
```
...
