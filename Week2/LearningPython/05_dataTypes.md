# Data Types

Python has several built-in data types. These are the four you'll use most often:

| Data Type | Description | Example |
|-----------|-------------|---------|
| `int` | Whole numbers | `7`, `-15`, `100` |
| `float` | Decimal numbers | `3.14`, `2.7`, `-0.5` |
| `bool` | Boolean (`True` or `False`) values | `True`, `False` |
| `str` | Text (strings) | `"Hello World"` |

> **Note:** These are the most common data types, but Python has many more. You can even create your own custom data types later on!

---

## Boolean Values

Boolean values are usually interchangeable or interpreted as the following pairs:

| Boolean | Numeric |
|----------|---------|
| `False` | `0` |
| `True` | `1` |

We often describe values as being either:

- **Falsy**
- **Truthy**

Many programming languages support these concepts, although the exact implementation can vary slightly between languages.

---

## Type Casting

Type casting converts a value from one data type to another (when the value allows it).

### Method 1 — Convert a Value

```python
a = float(7)
```

This is the most common and flexible method.

### Method 2 — Type Annotation

```python
a: float = 7
```

This tells Python that `a` is intended to be a float.

> **Note:** `7` becomes `7.0` when stored as a float.

You can also convert:

- Numbers → Strings
- Strings → Numbers *(only if the string contains a valid number)*
- Booleans ↔ Numbers
- Many other compatible data types

### Valid Conversion

```python
number = int("42")
print(number)
```

### Invalid Conversion

```python
number = int("Dog")
```

This will produce an error because `"Dog"` is not a valid number.

---

# Assignment 1

Using the variables below, print the following output:

```text
x + y = 42.7
```

### Starter Code

```python
x = 40
y = 2.7

z = True
aa = "Answer"
```

<details>
<summary>✅ Show Solution</summary>

```python
print("x + y =", x + y)
```

**Output**

```text
x + y = 42.7
```

</details>

---

## Notes

Notice that `x` is an `int` and `y` is a `float`.

Python automatically converts the result into a float when performing arithmetic between these two types.

```python
print(x + y)
```

Output:

```text
42.7
```

Some programming languages require you to explicitly convert the integer into a float first.

You can also convert a float into an integer:

```python
print(int(y))
```

Output:

```text
2
```

> **Note:** Converting a float to an integer removes the decimal part instead of rounding.

---

# Assignment 2

Using the same variables, print the following outputs:

```text
Answer 42
```

```text
True Answer
```

<details>
<summary>✅ Show Solution</summary>

### Answer 42

```python
print(aa, x + int(y))
```

**Output**

```text
Answer 42
```

### True Answer

```python
print(z, aa)
```

**Output**

```text
True Answer
```

</details>

---

## Notes

You can concatenate (combine) values inside a `print()` statement.

You can also include extra strings directly inside `print()` to add spaces, punctuation, or additional words.

Example:

```python
print("Hello", "World")
```

Output:

```text
Hello World
```

---

# Assignment 3

Using the variables above and additional strings inside `print()`, print:

```text
The True Answer is: 42
```

<details>
<summary>✅ Show Solution</summary>

```python
print("The", z, aa, "is:", x + int(y))
```

**Output**

```text
The True Answer is: 42
```

</details>

---

## Notes

The tricky part of this assignment is converting a float into an integer so that `42.7` becomes `42`.

Example of converting a float to an integer:

```python
value = 42.7
print(int(value))
```

Output:

```text
42
```

> **Good job if you figured this one out!**