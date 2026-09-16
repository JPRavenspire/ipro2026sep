# Hello, World!

You can print text to the console with the following line of code:

```python
print("Hello World!")
```

You can enclose strings with either `""` or `''`. If you want the string to span multiple lines, use `""" """` or `''' '''`.

## ASSIGNMENT 1

Write your first program!
Write a program that prints Hello, World! to the command line and run it!

## ASSIGNMENT 2

Write your second program:
Write a program that prints "Hello, World!" to the command line. So, not just the letters, but the actual quotation marks as well!

## NOTES

Did you run into any problems? If so, what do you think is going wrong? And if not, what did you do to get the `""` on screen?
Since python uses wrapping `""` to denote text, you run into problem if you actually want to print `""`.
To circumvent this issue, python, and other languages as well, use escape characters.
In the case of pyton, this is a backslash: `\`
So if you want to print an actual `"`, you simply have to precede it with a backslash, like so: `\"`

Here is a list of some of the most commonly used escape sequences:

| Sequence | Translation               |
| -------- | ------------------------- |
| `\'`     | `'` apostrophe            |
| `\"`     | `"` quote                 |
| `\n`     | newline character         |
| `\t`     | horizontal tab character  |
| `\r`     | carriage return character |
| `\\`     | `\` backslash             |

You may think this simply shifts the problem to not being able to type the `\` character.
But simply typing 2 backslashes like so: `\\` does the trick.

