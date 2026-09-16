# Type Conversion

We've worked primarily with numbers and strings so far. We've even printed them out in a single command.
But what about the following scenario?

```python
a = 7
b = "7"

print(a + b)
```

If we try this, we get an error! Why? Because "7" is not a number, but a string. And the computer doesn't know how to add a string (which is a word, or series of characters) together with a number.
Instead we'll have to do the following:

```python
a = 7
b = "7"

b = int(b)

print(a + b)
```

You can explicitly convert type into another using type conversion as shown above.  