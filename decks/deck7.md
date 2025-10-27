---
marp: true
title: Week 7
theme: gaia
paginate: true
footer: CMPT 120 - Fall 2025 - Week 7 - Nicholas Vincent
---
---

# Agenda

- Repeat comments on midterm adjustments
- A4 coming soon; "chiller autograder" (because we're learning functions today)
- Review: finding min and max from a file
- 20 min primer on functions
- Binary, bits/bytes, ASCII overview
- Hex colors (quick look)
- Practice with counting and parallel lists

---

### Next week: TBA by end of day today. 

- Most likely video lectures + I'll ask TAs to come to lecture hall so you can have more opportunities for in-person, over the shoulder coding

---

## Review: min and max

What would the pseudo-code look like?

---

Pseudo-code:

- Initialize a variable to hold max (or min). It should start smaller (or larger) than any item.
- Iterate through items.
- If item is larger (or smaller) than the current value, update the variable.
- After all items are seen, you have the max (or min).

---

```python
values = [3, 5, 2, 8, 6]
maximum = values[0]
for value in values:
    if value > maximum:
        maximum = value
print(maximum)  # 8
```

---

How to keep track of the index of the max or min?

---

```python
values = [3, 5, 2, 8, 6]
maximum = values[0]
index_of_max = 0
for i in range(len(values)):
    value = values[i]
    if value > maximum:
        maximum = value
        index_of_max = i
print(maximum, index_of_max)
```

---

## From a file?

---

```python
# Open the file safely using 'with' (auto-closes the file afterward)
with open("data.txt", "r") as file:
    # Read all lines into a list
    lines = file.readlines()

# Convert lines (strings) into integers
values = []
for line in lines:
    number = int(line.strip())  # remove whitespace/newline and convert to int
    values.append(number)

# Initialize max and min with the first value
maximum = values[0]
minimum = values[0]
index_of_max = 0
index_of_min = 0

# Iterate through the list to find max and min
for i in range(len(values)):
    value = values[i]

    # Update maximum if a larger value is found
    if value > maximum:
        maximum = value
        index_of_max = i

    # Update minimum if a smaller value is found
    if value < minimum:
        minimum = value
        index_of_min = i

# Print results
print("Maximum value:", maximum, "at index", index_of_max)
print("Minimum value:", minimum, "at index", index_of_min)

# Example note:
# If these numbers represented education levels or scores,
# 'maximum' would be the highest 'edu value'.
```



---

Quick reminder for practice.

If you're prone to exploring, you may have tried typing something like...

```python
max([1,2,3])
```

Which works!

---

- In practice, we'll often use pre-written functions and methods.
- It's safer to do so — writing a max-finding function from scratch in a high-stakes setting (factory, energy, transport, medicine) is risky.
- We're doing it in 120 so you understand what happens under the hood when you call these functions later on.
- Even if you end up coding mostly in spreadsheets, this mental model helps.

---


## Functions

Why use functions?

- Reuse: avoid repeating code by naming a task.
- Abstraction: hide details; focus on intent.
- Testability: small units are easier to verify and debug.
- Collaboration: clearer boundaries and responsibilities.

---

### Defining and calling

```python
def greet(name):
    return f"Hello, {name}!"

msg = greet("Ada")
print(msg)  # Hello, Ada!
```

- `def` creates a function; parameters go in `()`.
- `return` sends a value back to the caller.

---

### Parameters and defaults

```python
def power(base, exponent=2):
    return base ** exponent

print(power(3))        # 9 (uses default exponent=2)
print(power(2, 5))     # 32
print(power(exponent=3, base=2))  # 8 (keyword args)
```

- Positional vs. keyword arguments; defaults make APIs friendlier.

---

### Return vs. print and scope

```python
def double(n):
    result = n * 2  # local variable
    return result

x = double(4)
print(x)  # 8
```

- `return` gives a value to the caller; `print` just displays text.
- Variables created inside a function are local to it (scope).

---

### Docstrings and type hints (advanced, can ignore for now)

```python
def add(a: int, b: int) -> int:
    """Add two integers and return the sum."""
    return a + b

print(add(2, 3))  # 5
```

- Docstrings explain intent and usage; hints aid readability and tooling.

---

## Binary numbers and ASCII

- Why learn this? It's how information is stored on computers.

---

Immersion program starting now:

01001000 01100101 01101100 01101100 01101111 00100000 01010111 01101111 01110010 01101100 01100100

---

Fun fact — there's a binary message in the building where I studied computing science!

[A coded message hidden in floor tiles (UCLA)](https://newsroom.ucla.edu/stories/a-coded-message-hidden-in-floor-247232)

(Discovered by a student and posted to r/ucla.)

---

### Why binary?

What are (digital) computers?

- Machines that convert low and high electrical signals into 0s and 1s.
- Then we do some math with the 0s and 1s.

---

## Bits

A bit is a single unit of information that has either the value zero or one.

- 0
- 1

(A "1" might correspond to a charged capacitor; in practice, to store more information in a smaller space, we use transistors — semiconductor devices that can switch between conducting and insulating.)

---

## Bytes

- A byte is 8 bits

---

## Using decimal to represent numbers

In "decimal" (aka numbers you are used to seeing), e.g. 10, 250, 11713, each digit represents powers of ten.

In the number '345':

- the 3 represents 3 * 10^2 = 300, because 10^2 = 100
- the 4 represents 4 * 10^1 = 40
- the 5 represents 5 * 10^0 = 5

As we add digits to the left-hand side of our decimal numbers, we get higher powers of ten.

---

Left-hand side is just a convention, by the way! Imagine some mirror world where we decide that the number 123 is written as 321. There's no reason it couldn't be (left-to-right reading is also a convention).

---

## Using binary to represent numbers

In binary, the bits represent powers of 2:

- 1 ($2^0$)
- 2 ($2^1$)
- 4 ($2^2$ = 2 * 2)
- 8 ($2^3$ = 2 * 2 * 2)
- 16 ($2^4$ = 2 * 2 * 2 * 2)
- ...

---

## Example of 2-digit binary numbers

- 00 -> $0*1$ (rightmost digit) + $0*2$ (2nd from right) = 0
- 01 -> $1*1$ + $0*2$ = 1
- 10 -> $0*1$ + $1*2$ = 2
- 11 -> $1*1$ + $1*2$ = 3

---

Challenge:

- What is the maximum number we can store with 4 bits?
- What about a byte?
- Extreme challenge (try using your Python terminal): 4 bytes

---

```python
def max_number_for_bits(n_bits):
    return 2**n_bits - 1

# Example usage:
n_bits = 4
print(f"The maximum number that can be stored with {n_bits} bits is {max_number_for_bits(n_bits)}")
```

---

- ASCII is a table that maps decimal numbers to characters.
- So, if we have a binary number, we can map it to a decimal number and then to a character.

---

## Converting binary to decimal in Python

- Any ideas how we'd do it?

---

```python
binary_str = "1101"
decimal = 0
length = len(binary_str)

for i in range(length):
    bit = binary_str[i]
    if bit == '1':
        decimal += 2 ** (length - i - 1)

print(f"The decimal representation of binary {binary_str} is {decimal}")
```

---

With a few bells and whistles (preview content — you don't need to feel 100% comfortable with this right now):

```python
def binary_to_decimal(binary_str):
    decimal = 0
    length = len(binary_str)
    for i, bit in enumerate(binary_str):
        decimal += int(bit) * (2 ** (length - i - 1))
    return decimal
```

---

Example usage:

```python
binary_str = "1101"
print(f"The decimal representation of binary {binary_str} is {binary_to_decimal(binary_str)}")
```

---

(just FYI)

```python
def binary_to_decimal(binary_str):
    return int(binary_str, 2)

# Example usage:
binary_str = "1101"
print(f"The decimal representation of binary {binary_str} is {binary_to_decimal(binary_str)}")
```

---

## Another "code"

Anyone recognize this?

- #00FFAA
- #FF0000

---

It's hexadecimal!

Used for colors, among other uses.

---

## Using our recsys example (parallel lists) to handle this new content

```python
print("Let's find the most popular coffee shop")

survey_responses = [
    "tims", "sbux", "ren", "tims", "sbux", "blenz",
    "blenz", "ren", "blenz"
]
options = ["tims", "sbux", "ren", "blenz"]

list_of_counting_vars = [0] * len(options)

for response in survey_responses:
    for i in range(len(options)):
        if options[i] == response:
            list_of_counting_vars[i] += 1

for i in range(len(options)):
    print(options[i], list_of_counting_vars[i])
```

---

With ASCII

```python
dec = ["65", "66", "67"]
chars = ["A", "B", "C"]

characters_as_dec = ["65", "65", "65", "67", "67", "67"]

for i in range(len(characters_as_dec)):
    for j in range(len(dec)):
        if characters_as_dec[i] == dec[j]:
            print(chars[j])
```
