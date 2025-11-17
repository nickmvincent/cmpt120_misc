---
marp: true
title: Deck 12-13
paginate: true
---


---


Process note: I originally posted a giant deck 10-13 so you could see all the final content of the course. After finishing the weeks of Nov 3 and Nov 10, I reorganized all the slides we covered into deck10-11.pdf

This is deck 12-13, all the rest of our content!

## Binary Search

[Interactive Binary Search Demo](http://interactivepython.org/courselib/static/pythonds/SortSearch/TheBinarySearch.html)

---

## A Real-life Example

Let’s say you want to sort Pokémon cards.  
You could sort by HP — how might you do it?

---

## Swapping Pattern

Let’s say we want to swap the values at two different spots in a list.

```

temp ← a
a ← b
b ← temp

````

---

## Selection Sort

**Algorithm:**

- For every element in the list:
  - Find the smallest element in the rest of the list
  - Swap the current element with that smallest element

[Selection Sort Reference](http://interactivepython.org/courselib/static/pythonds/SortSearch/TheSelectionSort.html)

---

## Timing Programs

You can use the `time` module to measure how long your program takes.

```python
import time
start = time.time()
# your code
end = time.time()
print(end - start)
```

---

## Visualization of Sorting Algorithms

Source: [GitHub - vbohush/SortingAlgorithmAnimations](https://github.com/vbohush/SortingAlgorithmAnimations)
YouTube: [Sorting Algorithm Visualization](http://www.youtube.com/watch?v=ZZuD6iUe3Pc)


---

## Goodness of an Algorithm

1. **Correctness** — It works.
2. **Desirable qualities:**

   * Readable and easy to debug
   * Clear and structured
   * Robust and maintainable
   * Efficient in time and space

---

## Two Ways to Examine "Goodness"

* **Time Complexity** – efficiency of execution
* **Space Complexity** – efficiency of memory use

Efficiency is key for large-scale problems.

---

## Complexity

Amount of time or space required to run an algorithm.
We focus on **time complexity** in this course.

---

## Measuring Time Complexity

We often measure:

* Execution time for a given problem
* Or, number of operations performed (hardware-independent)

---

## Order of an Algorithm

Represents how the number of operations grows with input size `n`.

Examples: `O(n)`, `O(n²)`, `O(log n)`

---

## Standard Reference Functions

| Category     | Function  |
| ------------ | --------- |
| Constant     | 1         |
| Logarithmic  | log₂(n)   |
| Linear       | n         |
| Linearithmic | n log₂(n) |
| Quadratic    | n²        |
| Cubic        | n³        |
| Exponential  | aⁿ, a>1   |

[More on Big O](https://en.wikipedia.org/wiki/Big_O_notation)

---

## Example: Calculating Time Complexity

```python
x = 0
y = 10
x += 1
for i in range(n):
    x += y
    y += 1000
```

→ `O(n)` complexity.

---

## Example 2: Nested Loops

```python
count = 0
for i in range(n):
    count += 10
    for j in range(n):
        count += j
```

→ `O(n²)` complexity.

---

## Best, Worst, and Average Case

* **Best:** fastest scenario
* **Worst:** slowest scenario
* **Average:** expected scenario

Example: Linear Search

* Best: Found at first element
* Worst: Found at last element or not found

---

## Linear Search Complexity

| Case  | Complexity |
| ----- | ---------- |
| Best  | O(1)       |
| Worst | O(n)       |

---

## Logarithmic Complexity

Each iteration halves the problem size → **O(log n)**

Examples:

* Binary search
* Divide and conquer algorithms

---

## Binary Search Analysis

Each split halves the data until 1 element remains.
Height of the tree = `log₂ n` comparisons (worst case).

---

## Selection Sort Complexity

Selection sort compares:

```
n + (n-1) + (n-2) + ... + 1 = n(n+1)/2 ≈ O(n²)
```

Applies to both best and worst cases.

---

## Comparing Algorithms

| Algorithm      | Big O    |
| -------------- | -------- |
| Linear Search  | O(n)     |
| Binary Search  | O(log n) |
| Selection Sort | O(n²)    |

---

## Is Sorting Worth It?

Binary search requires sorted data, but sorting costs `O(n²)`.
Sorting first makes sense when:

* You search many times after sorting.

---

## When n Gets Larger

| Algorithm   | Big O    | Example (n=1000) |
| ----------- | -------- | ---------------- |
| Constant    | O(1)     | 1                |
| Linear      | O(n)     | 1000             |
| Quadratic   | O(n²)    | 1,000,000        |
| Logarithmic | O(log n) | ~10              |

---

## Introducing Merge Sort

Much faster than Selection Sort.
[Visualization](https://visualgo.net/en/sorting)

---

## Merge Sort Concept

1. Split list until each has one element
2. Merge sorted sublists

---

## Merge Sort Pseudocode

```python
def mergeSort(alist):
    if len(alist) > 1:
        left = mergeSort(alist[:mid])
        right = mergeSort(alist[mid:])
        return merge(left, right)
    else:
        return alist
```

---

## Merge Sort Complexity

* Splits → `log n`
* Merges → `n`
* **Total: O(n log n)**

Uses extra space for merging.

---

## Review

| Algorithm      | Worst Case Complexity |
| -------------- | --------------------- |
| Linear Search  | O(n)                  |
| Binary Search  | O(log n)              |
| Selection Sort | O(n²)                 |
| Merge Sort     | O(n log n)            |

---

## Final Thought

If two algorithms are **O(n)** and **O(n log n)**,
and you have a **large dataset**,
choose the **O(n)** algorithm.

---



# Week 12 Recursion

This folder includes some interactive content we'll work through together during Week 12!

We'll spend some time trying to code key recursive functions and live code them together.

This deck has the SAME content as the readme file in `other_content/week12_recursion`. I will recommend you open that file during lecture, and I'll project this just for slightly better lecture viewing experience.


---

## Exercise 1: Review tree drawing

First, take a look at `draw_tree.py` in this deck. We're going to talk through how and why this code works. You should copy and paste this into a file on your local machine. Trying running it, then try modifying the *initial function call* so that the tree:

1. Has even more branches
2. Has fewer branches
3. Hits the base case immediately

---

```python
import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Recursive Tree")

# Set up the turtle
tree_turtle = turtle.Turtle()
#tree_turtle.shape("turtle")
tree_turtle.speed("fastest")  # Speed up the drawing

# Recursive function to draw a fractal tree
def draw_tree(turtle, branch_length, angle):
    if branch_length > 5:  # Base case: stop when the branch is too short
        # Draw the main branch
        turtle.forward(branch_length)
        
        # Right branch
        turtle.right(angle)
        draw_tree(turtle, branch_length - 15, angle)
        
        # Left branch
        turtle.left(2 * angle)
        draw_tree(turtle, branch_length - 15, angle)
        
        # Reset position and angle for next branch
        turtle.right(angle)
        turtle.backward(branch_length)

# Initial position
tree_turtle.left(90)  # Point the turtle upwards
tree_turtle.penup()
tree_turtle.goto(0, -200)  # Move to starting position
tree_turtle.pendown()

# Draw the tree
draw_tree(tree_turtle, branch_length=100, angle=20)

# Finish up
turtle.done()
```

---


## Exercise 2: Recursive Factorial

Problem: Write a recursive function that returns the factorial of a number. The factorial of n is equal to n times the factorial of n-1.

Start with a single parameter function definition: `def factorial(n):`

Examples:
- 0! = 1 (important: the factorial of 0 is equal to 1.)
- 1! = 1
- 2! = 2 * 1= 2 * 1!
- 3! = 3 * 2 * 1 = 3 * 2!
- so, `factorial(4) # -> 24`

<details>
<summary>Hint 1: Base Case</summary>

The base case will be based on the definition that factorial(0) = 1. It occurs when `n` is 0.

</details>

<details>
<summary>Hint 2: Recursive Case</summary>

In order to move towards the base case, consider decrementing the variable being passed by argument (`n`) by 1.

(e.g., somewhere in your code call, `factorial(n-1)`)
</details>

---

<details>
<summary> Solution</summary>

```python
def factorial(n):
    if n == 0:  # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive case

# Example usage:
print(factorial(5))  # Output: 120
```
</details>


--- 

## Exercise 3: Sums with recursion

### Exercise 3a: Summing all integers from 1 to n
Write a recursive function in Python, recursive_sum, that calculates the sum of all integers from 1 up to a given positive integer n.

Start with a single parameter function definition:`def recursive_sum(n):`

Examples: 
- `recursive_sum(4)  # Output: 10 (1 + 2 + 3 + 4)`
- `recursive_sum(5)  # Output: 15 (1 + 2 + 3 + 4 + 5)`

<details>
<summary>Hint 1: Base Case</summary> The base case occurs when `n` is 0. The sum of all integers up to 0 is simply 0. </details>

<details>
<summary>Hint 2: Recursive Case</summary>

If `n` is greater than 0, return `n` plus the result of `recursive_sum(n - 1)`.
</details>

---

<details>
<summary>Solution</summary>

```python
def recursive_sum(n):
    if n == 0:  # Base case
        return 0
    else:
        return n + recursive_sum(n - 1)  # Recursive case

# Example usage:
print(recursive_sum(5))  # Output: 15
```
</details>


---

### Exercise 3b: Summing all integers in a list
Problem: Write a recursive function in Python, recursive_sum_list, that calculates the sum of all integers in a given list.

Start with a single parameter function definition: `def recursive_sum_list(numbers):`

Examples:
- `recursive_sum_list([1, 2, 3, 4]) # Output: 10`
- `recursive_sum_list([5, 7, 3]) # Output: 15`

<details> <summary>Hint 1: Base Case</summary> The base case occurs when the list is empty. The sum of an empty list is simply 0. </details> <details>

<summary>Hint 2: Recursive Case</summary> If the list is not empty, return the first element of the list plus the result of `recursive_sum_list` called on the rest of the list. </details>

<details>

<summary>Hint 3: List Indexing</summary>

To get the first element of the list, use `numbers[0]`. To get the "rest of the list", use `numbers[1:]`.

</details>

---

<details>
<summary>Solution</summary>

```python
def recursive_sum_list(numbers):
    if not numbers:  # Base case
        return 0
    else:
        return numbers[0] + recursive_sum_list(numbers[1:])  # Recursive case

# Example usage:
print(recursive_sum_list([1, 2, 3, 4]))  # Output: 10
```

</details>

---

## Exercise 4: Reverse a string

Write a recursive function in Python, recursive_reverse, that reverses a given string. Start with a single parameter function definition: `def recursive_reverse(s):`

Example:
- `recursive_reverse("hello")  # Output: "olleh"`
- `recursive_reverse("abc")  # Output: "cba"`

<details>
<summary>Hint 1: Base Case</summary> The base case is an empty string or a single-character string, which is its own reverse.
</details>

<details>
<summary>Hint 2: Recursive Case</summary> Return the last character of the string concatenated with the reverse of the rest of the string.
</details>


<details>
<summary>Hint 3: String Indexing</summary>.

To get the last character of the string, we can use `s[-1]`. To get the "rest of the string", we can use `s[:-1]`.

</details>

---

<details>
<summary>Solution</summary>

```python
def recursive_reverse(s):
    if len(s) <= 1:  # Base case
        return s
    else:
        return s[-1] + recursive_reverse(s[:-1])  # Recursive case

# Example usage:
print(recursive_reverse("hello"))  # Output: "olleh"
```
</details>

---

## Exercise 5: Palindrome checker

Write a recursive function in Python, is_palindrome, that checks if a given string is a palindrome (reads the same forward and backward). Start with a single parameter function definition: `def is_palindrome(s):`


Examples:
- `is_palindrome("racecar")  # Output: True`
- `is_palindrome("hello")    # Output: False`


<details>
<summary>Hint 1: Base Case</summary>
The base case is when the string is empty or has a length of 1; both cases are palindromes by definition.
</details>

<details>
<summary>Hint 2: Recursive Case</summary> If the first and last characters are the same, check if the substring between them is a palindrome by calling `is_palindrome` recursively.
</details>

<details>
<summary>Hint 3: String Indexing</summary>
To check the substring between the first and last character, you can use the indexing approach `s[1:-1]` </details>


---

<details>
<summary>Solution</summary>

```python
def is_palindrome(s):
    if len(s) <= 1:  # Base case
        return True
    elif s[0] == s[-1]:  # Recursive case
        return is_palindrome(s[1:-1])
    else:
        return False

# Example usage:
print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello"))    # Output: False
```
</details>


---

## Exercise 6: Challenge!

"Nested List Sum"

Problem: Write a recursive function in Python, nested_sum, that calculates the sum of all integers in a list. However, this time, some elements of the list might be nested lists themselves. The function should recursively process these nested lists to calculate the total sum.

You can use `isinstance(item, int)` to check an item is an integer and `isinstance(item, list)` to check if an item is a list.

Start with a single parameter function definition: def nested_sum(data):

Examples:
- nested_sum([1, 2, [3, 4], 5]) # Output: 15
- nested_sum([[1, 2, [3]], 4, [5, [6]]]) # Output: 21
- nested_sum([1, [2, [3, [4, [5]]]]]) # Output: 15

<details> <summary>Hint 1: Base Case</summary> The base case is when the current item is an integer, in which case you can return the integer itself. </details>

<details> <summary>Hint 2: Recursive Case</summary> If the current item is a list, loop through each element in the list and recursively apply `nested_sum` on each element, summing the results. </details>


---

<details><summary>Solution</summary>

```python
def nested_sum(data):
    total = 0
    for item in data:
        if isinstance(item, int):  # Base case
            total += item
        elif isinstance(item, list):  # Recursive case
            total += nested_sum(item)
    return total

# Example usage:
print(nested_sum([1, 2, [3, 4], 5]))          # Output: 15
print(nested_sum([[1, 2, [3]], 4, [5, [6]]])) # Output: 21
print(nested_sum([1, [2, [3, [4, [5]]]]]))    # Output: 15
```

</details>


---

## Exercise 7: Count Vowels in a String

Problem: Write a recursive function, count_vowels, that counts the number of vowels (a, e, i, o, u) in a given string. The function should be case-insensitive, so both uppercase and lowercase vowels are counted.

Start with a single parameter function definition: `def count_vowels(s):`

Examples:
- `count_vowels("hello") # Output: 2`
- `count_vowels("Recursion is fun!") # Output: 6`
- `count_vowels("xyz") # Output: 0`

<details> <summary>Hint 1: Base Case</summary> The base case occurs when the string is empty. If it is, return 0 because there are no vowels in an empty string. </details>

<details> <summary>Hint 2: Recursive Case</summary> Check if the first character of the string is a vowel. If it is, add 1 to the count, and then call the function recursively on the rest of the string. </details>

---

<details> <summary>Solution</summary>

```python
def count_vowels(s):
    vowels = "aeiouAEIOU"
    if not s:  # Base case: empty string
        return 0
    elif s[0] in vowels:  # Check if first character is a vowel
        return 1 + count_vowels(s[1:])
    else:
        return count_vowels(s[1:])  # Recursive case: continue with next character

# Example usage:
print(count_vowels("hello"))            # Output: 2
print(count_vowels("Recursion is fun!"))  # Output: 6
print(count_vowels("xyz"))              # Output: 0
```

</details>


# Binary Search: A Fast Way to Find Things

---

## Agenda / About this deck

First, finish our recursion activity.

Then, run through this deck very quickly. This is just focused on the code implementation of binary search (lots of overlap with Runestone).

Then, depending on time, we'll talk more conceptually about search, but also just work on project.


---

## Introduction to Searching
- **Searching**: Imagine looking for a word in a dictionary. If you check one word at a time from the start, it would take ages for a long dictionary. Binary Search makes this faster.
- **Key Idea**: Divide the search space in half each time.

--- 

## Linear Search vs. Binary Search
- **Linear Search**: O(n)
  - Check each element one-by-one.
  - Useful when data is unsorted.
- **Binary Search**: O(log n)
  - Faster, but requires sorted data.
  - Each time, cut the search space in half.

---

> **Interactive Demo**: Imagine finding a word in a dictionary. How many words do you skip if you flip halfway each time?

---

## Binary Search Intuition
- **Sorted Array Example**: [1, 3, 5, 7, 9, 11, 13]
  - Target: Find 9.
  - **Step 1**: Start with middle element (7).
  - **Step 2**: Since 9 > 7, ignore left half.
  - **Step 3**: Now search [9, 11, 13]. Middle is 11.
  - **Step 4**: Since 9 < 11, ignore right half. Find 9.

---

## Visualization
- **Divide-and-Conquer**:
  - Use visuals to demonstrate the division of the array.
  - Show the array shrinking in size each time.
- **Pseudocode**:
  ```
  low = 0
  high = len(array) - 1
  while low <= high:
      mid = (low + high) // 2
      if array[mid] == target:
          return mid
      elif array[mid] < target:
          low = mid + 1
      else:
          high = mid - 1
  return -1
  ```

---

## Why Does It Work?
- **Core Concept**: Every decision eliminates half of the possible choices.
- **Comparison to Real Life**: Imagine finding a page in a book without an index. Flip to the middle until you narrow it down.

---

## Practice Problem
- **Problem**: Find the number 23 in the sorted list [5, 12, 15, 23, 27, 30, 35].
- **Thinking out loud**: Can try to write out / verbalize each step.
  - “Is 23 greater or less than the middle element?”
  - Keep cutting until found.

---

## Common Mistakes
- **Off-by-One Errors**: Carefully manage `low` and `high` boundaries.
- **Infinite Loops**: Ensure condition `low <= high`.

> **Tip**: Debugging exercises can help solidify this. Run a failing example and walk through the fix.

---

Example mistake 1: Incorrect Mid Calculation

```python
array = [1, 3, 5, 7, 9, 11, 13]
target = 9

low = 0
high = len(array) - 1
while low <= high:
    mid = (low + high) / 2  # Mistake: Using `/` instead of `//` for integer division
    if array[mid] == target:
        print(f"Found target {target} at index {mid}")
        break
    elif array[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Target not found")
```

---

Mistake 2: Off-by-One Error

```python
# Mistake 2: Off-by-One Error
array = [1, 3, 5, 7, 9, 11, 13]
target = 9

low = 0
high = len(array)  # Mistake: Should be `len(array) - 1`
while low <= high:
    mid = (low + high) // 2
    if array[mid] == target:
        print(f"Found target {target} at index {mid}")
        break
    elif array[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Target not found")
```

---

Example Mistake 3: Infinite Loop Condition

```python
array = [1, 3, 5, 7, 9, 11, 13]
target = 9

low = 0
high = len(array) - 1
while low < high:  # Mistake: Should be `low <= high`
    mid = (low + high) // 2
    if array[mid] == target:
        print(f"Found target {target} at index {mid}")
        break
    elif array[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Target not found")
```

---

# Fully Worked Example of Binary Search

```python
def binary_search(array, target):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        # Debug statement to show the current state of low, high, and mid
        print(f"Low: {low}, High: {high}, Mid: {mid}, Mid Value: {array[mid]}")

        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Target not found

# Example usage
array = [1, 3, 5, 7, 9, 11, 13]
target = 9
result = binary_search(array, target)
if result != -1:
    print(f"Target {target} found at index {result}")
else:
    print("Target not found")
``` 

---

## Binary Search Applications
- **Applications**:
  - Finding an element in a sorted array.
  - Searching in a phonebook.
  - Problems like "Guess the Number" (using minimum attempts).

---

## Conclusion & Recap
- **Summary**: Binary Search cuts the search space in half each time, leading to a time complexity of O(log n).
- **Key Question**: Why does Binary Search need a sorted array?

> **Engagement**: Think of any real-life activities where a binary search-like strategy is used?

---

https://www.cs.usfca.edu/~galles/visualization/Search.html

---



# The Big Review Deck


<div style="display:flex; justify-content: center;">
<img src="/images/priscilla-du-preez-Vm0nC-VKFTc-unsplash.jpg" style="max-width:200px"/>
</div>

From Priscilla Du Preez @ https://unsplash.com/photos/scenery-of-bridge-in-front-of-silhouette-of-mountain-Vm0nC-VKFTc



---


# Week 1: Introduction to CS and Problem Solving

<div class="grid grid-cols-2 gap-4">
<div>

- Know that CS is problem-solving
- Problem solving by subdividing tasks
- Characteristics of an algorithm
- Plagiarism rules for programming
- What is pseudocode?
- Write Python comments, program header block info
- Output "Hello World" using print()
- Programming languages vs. natural languages
- Use IDLE and an IDE
- Submit code as .zip or .py file

</div>
<div>

```python
# Problem Solving Example: Basic Algorithm & Hello World
def greet():
    """Program header block: Author, Date, Purpose."""
    print("Hello, World!")  # Simple print statement

# Algorithm breakdown using function
greet()
```

</div></div>


---

# Week 2: Basics of Python Programming

<div class="grid grid-cols-2 gap-4">
<div>

- Design/plan algorithms using pseudocode/comments
- Input from terminal to a variable or without saving
- Assign a value to a variable
- Output a string variable, string concatenation
- Variable naming rules
- Data types introduction (focus on String)
- Lists and random.choice() (including imports)
- Purpose of modules, imports at top
- If/elif/else, logical operators (`and`, `or`)
- Comparison operators in conditional statements
- Boolean expressions, testing programs interactively
- Characteristics of good software
- Interpreter’s role in error catching

</div>

<div>

```python
# Variables, Input, Output, and Conditionals
name = input("Enter your name: ")  # Obtain user input
age = int(input("Enter your age: "))  # Type conversion from string to int

if age >= 18:
    print(f"Welcome, {name}. You are eligible!")  # Use of formatted string
else:
    print(f"Sorry, {name}. You are not eligible.")  # Conditional branching
```

</div> </div>

---

# Week 3: Strings, Lists, and Conditionals

<div class="grid grid-cols-2 gap-4">
<div>

- String methods: `strip()`, `lower()`, `upper()`
- Identify String data type
- Test methods using REPL
- Use `in` keyword with strings and lists
- Create a list from variables/user inputs
- Loop over list elements with `for`
- Understand `range()` function and index variable
- Integer type and conversion to String
- Concatenation rules, nested conditionals
- Error types: syntax vs. semantic
- Method chaining with `.`

</div>
<div>

```python
# String Methods and Looping Over Lists
fruits = ["Apple", "Banana", "Cherry"]
for fruit in fruits:
    print(fruit.lower())  # Using string methods to manipulate list elements

# Check if a character is in a string
if "a" in "banana":
    print("Found 'a' in banana")
```

</div></div>

---

# Week 4: Loops and Arithmetic

<div class="grid grid-cols-2 gap-4">
<div>- U
se `range()` with variables
- Loop to reduce code duplication
- Integers, floats, initialization
- Accumulator pattern, `+=` shortcut
- Get list length, convert input to Integer
- Division types, arithmetic operations
- Print floats to given decimals

</div>
<div>

```python
# Accumulator Pattern and Loop with Range
total = 0
for i in range(1, 6):  # Loop from 1 to 5
    total += i  # Accumulate the sum

print(f"Sum of numbers from 1 to 5 is: {total}")

# Basic arithmetic operations
div_result = 10 / 3  # Division (float)
print(f"Division result: {div_result:.2f}")  # Print to 2 decimal places
```
</div></div>

---

# Week 5: File I/O, Lists, and Comparisons

<div class="grid grid-cols-2 gap-4">
<div>

- Read lines from text files
- String splitting, list indexing/slicing
- Compare numbers and strings
- operator precedence (light treatment)
- Nested conditionals, nested loops
- find comment elements between lists
- List concatenation, accumulation pattern for strings/lists
- Calculate max/min, coordination between lists by index

</div>
<div>

```python
# Reading a File and Splitting Lines into Lists
with open("example.txt", "r") as file:
    for line in file:
        words = line.strip().split()  # Split line into words
        print(words)  # List of words
```
</div></div>

---

# Week 7: Bits, Bytes, and Data Representation

<div class="grid grid-cols-2 gap-4">
<div>

- `len()` function, string immutability, loops by index
- Bits and bytes, converting bytes to bits
- Binary to decimal, hexadecimal goals
- ASCII and Unicode overview
- RGB storage in hexadecimal
- Important numbers: 1 byte = 8 bits, 8-bit per character for 8-bit character set, 6 hexadecimal digits in an RBG number, therefore 24 bits, because 6 digits x 4 bits per digit
- Different numbering systems (base-2, base-10, base-16) require different number of "symbols"

</div>

<div>

```
# Convert Bytes to Bits and Decimal to Binary
bytes_value = 4
bits_value = bytes_value * 8  # Convert bytes to bits
print(f"{bytes_value} bytes is {bits_value} bits")

# FF0001 -- what is this?
# 00FF00 -- what is this?
```

</div></div>

---

# Week 8: Turtle Graphics and Functions

<div class="grid grid-cols-2 gap-4">
<div>

- Use Turtle package for drawing (specific methods that are "testable" to be described in class)
- Read Turtle code and understand the purpose
- Create and call functions (with/without parameters)
- Loop variable as function argument
- Turtle coloring using RGB values
- Variable scope (function vs. global)

</div>
<div>

```python
# Turtle Graphics Drawing a Square
import turtle

def draw_square(size):
    pen = turtle.Turtle()
    for _ in range(4):
        pen.forward(size)
        pen.right(90)

draw_square(100)  # Draw a square with side length of 100
turtle.done()
```
</div></div>

---

# Week 9: Functions and While Loops

<div class="grid grid-cols-2 gap-4">
<div>

- Define and use functions, `return` vs `print()`
- Effect of `return` in loops, handling `None`
- Identify appropriate use of `while` vs `for`
- Sentinel and multiple control variables in `while`
- Use `while` for input validation

</div>
<div>

```python
# Function that Returns a Value and While Loop for Validation
def double_number(num):
    return num * 2

valid_input = False
while not valid_input:
    user_input = input("Enter a positive number: ")
    if user_input.isdigit() and int(user_input) > 0:
        valid_input = True
        result = double_number(int(user_input))
        print(f"Double of {user_input} is {result}")
    else:
        print("Invalid input, please enter a positive number.")
```
</div></div>

---

# Week 10: Modules and Image Processing

<div class="grid grid-cols-2 gap-4">
<div>

- Create and use custom modules
- Module shortnames and relationship of modules to filesystem
- RGB colors and pixel manipulation
- Access/modify 2D/3D lists for images
- Using course-specific `cmpt120images` module for images
- Return Boolean expressions directly

</div>
<div>

```python
# Custom Module Import and RGB Color Manipulation
import cmpt120images

image = cmpt120images.loadImage("example.png")
height = len(image)
width = len(image[0])

for y in range(height):
    for x in range(width):
        # Invert the RGB colors of the pixel
        r, g, b = image[y][x]
        image[y][x] = (255 - r, 255 - g, 255 - b)

cmpt120images.saveImage(image, "inverted_example.png")
```
</div></div>

---

# Week 11: Lists, Aliases, and Recursion

<div class="grid grid-cols-2 gap-4">
<div>

- Alias vs. copy of lists
- Function parameter and argument as aliases
- List modification inside functions
- Basic recursion, draw recursive patterns
- 3 characteristics of recursive function
- Write factorial, sum of list, reverse string using recursion
- Check if a string is a palindrome (recursive/iterative)

</div>
<div>

```python
# Recursive Function to Calculate Factorial
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(f"Factorial of 5 is: {factorial(5)}")
```
</div></div>

---

# Week 12: Search Algorithms

<div class="grid grid-cols-2 gap-4">
<div>

- Review recursion
- Write linear search functions (Boolean/index/indices)
- Recognize and code recursive binary search

</div>
<div>

```python
# Binary Search Implementation
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

numbers = [1, 3, 5, 7, 9, 11]
index = binary_search(numbers, 7)
print(f"Element found at index: {index}" if index != -1 else "Element not found")
```
</div></div>

---

# Week 13: Sorting and Complexity

<div class="grid grid-cols-2 gap-4">
<div>

- Swap list elements, selection sort
- Intermediate steps of selection sort
- Measure runtime with `time`
- Apply algorithms on data from a file
- Characteristics of a good algorithm
- Big O notation and complexity examples. 7 reference functions.
- Merge Sort approach and complexity
- Critical operations, best/worst case scenarios
- Analyze binary search and merge two lists

</div>
<div>

```python
# Selection Sort Implementation
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

data = [64, 25, 12, 22, 11]
selection_sort(data)
print(f"Sorted array: {data}")
```
</div></div>