# CMPT 120 – Final Exam Practice Questions

This file contains five practice questions that cover variables, lists, strings, loops, files, search, complexity, functions, recursion, images as 3D lists, bits/hex, and turtle graphics.

---

## Practice Q1: Variables, Lists, Integer Division, and Aliasing

Consider the following Python code:

```python
x = 10
y = 4

data = [x, y]
alias = data

x = x + y
data[0] = data[0] // 3
alias.append(x)

print("data:", data)
print("alias:", alias)
```

1. **(a)** Trace the execution of this program and write down exactly what is printed by the two `print` calls.

<details>
<summary>Answer (a)</summary>

The output is:

```text
data: [3, 4, 14]
alias: [3, 4, 14]
```

**Explanation:**

* Start: `x = 10`, `y = 4`, `data = [10, 4]`, `alias` references the **same list** as `data`.
* `x = x + y` → `x = 10 + 4 = 14` (this does **not** change `data`).
* `data[0] = data[0] // 3` → `data[0] = 10 // 3 = 3`, so the shared list becomes `[3, 4]`.
* `alias.append(x)` → appends `14` to the same list, making it `[3, 4, 14]`.
  Both `data` and `alias` refer to `[3, 4, 14]`, so they print the same.

</details>

---

2. **(b)** After the program finishes, what is the final value of the variable `x`? Explain briefly how it was computed.

<details>
<summary>Answer (b)</summary>

Final value of `x` is:

```text
14
```

**Explanation:**
`x` starts at `10`. The line `x = x + y` computes `x = 10 + 4`, so `x` becomes `14`. No later line changes `x`.

</details>

---

3. **(c)** The list `alias` was never assigned using square brackets, but both `data` and `alias` print the same contents. In 1–2 sentences, explain why changing `data` also affects `alias`.

<details>
<summary>Answer (c)</summary>

`alias = data` makes **both variables refer to the same list object** in memory. Any in-place change to the list (like `data[0] = ...` or `alias.append(...)`) affects that one shared list, so both names show the same contents.

</details>

---

## Practice Q2: Strings, Loops, Indexing, and Conditionals

Consider the function:

```python
def transform(words):
    result = ""
    for i in range(len(words)):
        word = words[i]
        if i % 2 == 0 and "a" in word.lower():
            result += word.upper()
        else:
            result += word.lower()
        if i != len(words) - 1:
            result += "|"
    return result

data = ["Alpha", "BETA", "gamma", "Pi"]
print(transform(data))
```

1. **(a)** In plain English (no code), describe the rule this function uses to decide whether to convert each word to upper-case or lower-case.

<details>
<summary>Answer (a)</summary>

* If a word is at an **even index** (0, 2, 4, …) **and** it contains the letter “a” (in any case), it is converted to **UPPER-CASE**.
* Otherwise (odd index, or no “a”), it is converted to **lower-case**.
  Words are joined with `|` between them.

</details>

---

2. **(b)** Show the exact string that is printed when this program runs, including all letters and the `|` separators.

<details>
<summary>Answer (b)</summary>

The printed string is:

```text
ALPHA|beta|GAMMA|pi
```

**Explanation (step by step):**

* `i = 0`, `"Alpha"` → even index and contains “a” → `"ALPHA"`
* `i = 1`, `"BETA"` → odd index → `"beta"`
* `i = 2`, `"gamma"` → even index and contains “a” → `"GAMMA"`
* `i = 3`, `"Pi"`   → odd index → `"pi"`

Bars `|` are added between words, but not after the last one.

</details>

---

3. **(c)** Suppose we change the second `if` condition to `if i < len(words):`. Will the output for the same `data` list change? Answer *yes* or *no* and briefly justify.

<details>
<summary>Answer (c)</summary>

**Yes**, it will change.

**Explanation:**
`range(len(words))` produces indices `0, 1, 2, 3` when there are 4 words. With `if i < len(words):`, the condition is true for **every** `i` in the loop (0, 1, 2, 3), so a `|` is added **after every word**, including the last one. The result would become:

```text
ALPHA|beta|GAMMA|pi|
```

with a trailing `|`.

</details>

---

4. **(d)** The function uses `range(len(words))` and indexing. Rewrite the `for` loop header using `enumerate(words)` instead (you do not need to rewrite the entire function body).

<details>
<summary>Answer (d)</summary>

You can rewrite the loop header as:

```python
for i, word in enumerate(words):
    ...
```

Then `i` is the index and `word` is the string at that position.

</details>

---

## Practice Q3: Files, Linear Search, Binary Search, and Time Complexity

1. **(a)** Write a function `count_nonempty(filename)` that:

   * opens the text file with the given `filename` using a `with` statement,
   * counts how many lines are **not** empty after stripping whitespace,
   * returns that count as an integer.

   You should iterate over the file line by line (do not read the entire file into memory at once).

<details>
<summary>Answer (a)</summary>

```python
def count_nonempty(filename):
    count = 0
    with open(filename, "r") as f:
        for line in f:
            if line.strip() != "":
                count += 1
    return count
```

**Explanation:**

* `with open(...)` safely opens and closes the file.
* `line.strip()` removes spaces, tabs, and newlines from both ends.
* If the stripped line is not an empty string, we increment the counter.

</details>

---

2. **(b)** The following function is meant to perform a simple linear search:

   ```python
   def contains(values, target):
       for value in values:
           if ???:
               return True
       return False
   ```

   Replace `???` with an appropriate condition so that the function returns `True` exactly when `target` appears in the list `values`, and `False` otherwise.

<details>
<summary>Answer (b)</summary>

Replace `???` with:

```python
value == target
```

So the function is:

```python
def contains(values, target):
    for value in values:
        if value == target:
            return True
    return False
```

</details>

---

3. **(c)** In one or two sentences, explain why a binary search function **requires** its input list to be sorted. Refer to how the algorithm works, not just “because that’s the rule.”

<details>
<summary>Answer (c)</summary>

Binary search repeatedly compares the target to the **middle** element and then discards **half** of the list based on whether the target is smaller or larger. This only works if all smaller elements are guaranteed to be on one side and all larger elements on the other—that is, the list must be sorted; otherwise, you might throw away the half that actually contains the target.

</details>

---

4. **(d)** Selection sort has time complexity (\mathcal{O}(n^2)), whereas a good implementation of binary search has time complexity (\mathcal{O}(\log n)). In a brief paragraph, compare what these complexities mean in practice as `n` (the list size) becomes large.

<details>
<summary>Answer (d)</summary>

With (\mathcal{O}(n^2)) (selection sort), doubling the list size roughly **quadruples** the amount of work, so sorting very large lists becomes slow quickly. With (\mathcal{O}(\log n)) (binary search), the work grows very slowly: doubling `n` only adds about **one extra step**. For example, searching in a list of a million items might take only around 20 comparisons, while sorting a million items with an (n^2) algorithm would require on the order of (10^{12}) operations.

</details>

---

## Practice Q4: Functions, Returning vs Printing, and Recursion

1. **(a)** Consider the function below:

   ```python
   def mystery(s):
       if s == "":
           return ""
       if s[0].isdigit():
           return mystery(s[1:])
       else:
           return s[0].upper() + mystery(s[1:])

   print(mystery("cs120-2025!"))
   ```

   i. Write down exactly what is printed when this code runs.
   ii. In 1–2 sentences, describe what `mystery` does to its input string in general.

<details>
<summary>Answer (a)</summary>

**i. Output**

```text
CS-!
```

**How we got it:**

* Input: `"cs120-2025!"`
* Digits (`'1','2','0','2','0','2','5'`) are **skipped**.
* Non-digits are converted to **upper-case**: `'c' → 'C'`, `'s' → 'S'`, `'-' → '-'`, `'!' → '!'`.
* Result: `"CS-!"`.

**ii. Description of what `mystery` does**

`mystery` removes all **digits** from the string and converts every remaining character to **upper-case**, returning the resulting string.

</details>

---

2. **(b)** Write a **recursive** function `sum_list(nums)` that takes a list of integers and returns the sum of all the numbers. You **must not** use loops or the built-in `sum`. Your function must correctly handle the empty list.

<details>
<summary>Answer (b)</summary>

```python
def sum_list(nums):
    # Base case: empty list has sum 0
    if nums == []:
        return 0
    # Recursive case: first element + sum of the rest
    return nums[0] + sum_list(nums[1:])
```

</details>

---

3. **(c)** Write a **non-recursive** version of `sum_list(nums)` that uses a loop to compute the same result.

<details>
<summary>Answer (c)</summary>

```python
def sum_list(nums):
    total = 0
    for n in nums:
        total += n
    return total
```

</details>

---

4. **(d)** Explain the difference between a function that **prints** a value and a function that **returns** a value. Give one short example where returning is more useful than printing.

<details>
<summary>Answer (d)</summary>

A function that **prints** a value sends text to the screen and then is done; you can’t directly use that printed value in other calculations. A function that **returns** a value hands the result back to the caller so it can be stored, combined, or passed to other functions.

**Example:**
A function `area_circle(r)` that **returns** the area lets you do:

```python
total = area_circle(1) + area_circle(2)
```

If `area_circle` only printed the area instead of returning it, you couldn’t easily add the two areas together.

</details>

---

## Practice Q5: 3D List Images, Bits/Hex, and Turtle Graphics

A colour image is stored as a “3D list” in Python: `image[row][col]` is a list of three integers `[R, G, B]` where each component is between `0` and `255`.

1. **(a)** Write a function `recolor_black_to_green(image)` that **modifies** the given image in-place so that every pure black pixel `[0, 0, 0]` becomes pure green `[0, 255, 0]`. Assume `image` has at least one row and one column.

<details>
<summary>Answer (a)</summary>

```python
def recolor_black_to_green(image):
    for r in range(len(image)):
        for c in range(len(image[r])):
            if image[r][c] == [0, 0, 0]:
                image[r][c] = [0, 255, 0]
```

**Explanation:**
We loop over all rows and columns; whenever we see a pixel that is exactly `[0, 0, 0]`, we replace it with `[0, 255, 0]`. Because we assign directly into `image`, the change happens in-place.

</details>

---

2. **(b)** Each colour component (R, G, B) is stored in exactly one byte.

   i. How many distinct intensity values can a single colour component represent? Answer in terms of the number of bits in a byte.
   ii. Approximately how many **bytes** are needed to store a `100 x 200` colour image in this format? Show the calculation, but you do not need to simplify the final number completely.

<details>
<summary>Answer (b)</summary>

**i.**
A byte has 8 bits, so a single color component can represent:

[
2^8 = 256
]

different intensity values (0–255).

**ii.**
Each pixel needs 3 bytes (R, G, B). For a `100 x 200` image:

[
100 \times 200 \times 3 \text{ bytes}
]

That equals:

[
100 \times 200 \times 3 = 60{,}000 \text{ bytes}
]

So approximately **60,000 bytes**.

</details>

---

3. **(c)** The following turtle code is executed (assume `t` is a turtle object and the window is large enough):

   ```python
   import turtle

   t = turtle.Turtle()
   t.color("blue")

   for i in range(4):
       t.forward(50)
       t.right(90)
       t.penup()
       t.forward(10)
       t.pendown()
   ```

   Describe the pattern that appears on the screen (shape(s), orientation, and spacing) and explain the role of `penup()` and `pendown()` in producing that pattern.

<details>
<summary>Answer (c)</summary>

**Pattern description:**
The turtle draws four **blue line segments** that form the sides of a square-like path, with each side of length 50. After each side, there is a **10-unit gap** before the next side starts, so the corners are not connected; you get a square outline broken at each corner. The square is axis-aligned (sides horizontal/vertical).

**Role of `penup()` and `pendown()`:**

* `t.penup()` lifts the pen so that the next `forward(10)` moves the turtle **without drawing**—this creates the small gaps.
* `t.pendown()` puts the pen back down so that the next `forward(50)` draws the next side.

</details>

---

4. **(d)** The RGB value `#FF0000` represents pure red in hexadecimal notation. Briefly explain how the pairs of hexadecimal digits in `#RRGGBB` correspond to the red, green, and blue components, and how this relates to the 3D list representation described in part (a).

<details>
<summary>Answer (d)</summary>

In `#RRGGBB`:

* The first two hex digits `RR` give the **red** value,
* The next two `GG` give the **green** value,
* The last two `BB` give the **blue** value.

Each pair is a hexadecimal number from `00` to `FF`, which corresponds to a decimal value from 0 to 255. For example, `#FF0000` has red = `FF` = 255, green = `00` = 0, blue = 0 → `[255, 0, 0]` in the 3D list representation (`[R, G, B]`).

</details>
