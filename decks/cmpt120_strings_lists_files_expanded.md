---
marp: true
theme: default
paginate: true
---

# CMPT 120 — Strings, Lists, Files & Recommendations

---

## Agenda
1. String splitting & advanced operations
2. list & string indexing refresher
3. File reading methods in Python
4. Recommendation systems
5. Comparisons & logical operators (refresher)
6. Practice review questions
7. Live coding activity (scaffold)
8. References

---

# 1. String Splitting & Advanced Operations

## The `split()` Method
- `str.split()` breaks a string into a list based on a delimiter.
- Default delimiter = whitespace.
```python
"apples bananas cherries".split()
# ['apples', 'bananas', 'cherries']
```

---

## Custom Delimiters
```python
data = "2025-09-29"
data.split("-")
# ['2025', '09', '29']
```

---

## The `join()` Method
```python
words = ["apples", "bananas", "cherries"]
", ".join(words)
# 'apples, bananas, cherries'
```

---

## Advanced String Operations
- **Slicing**: `s[start:end:step]`
- **Reversing**: `s[::-1]`
- **Membership**: `'cat' in 'concatenate'`
- **Case changes**: `.lower()`, `.upper()`, `.title()` (not on test)
- **Stripping**: `.strip()`, `.lstrip()` (not on test), `.rstrip()` (not on test)

---

# 2. Indexing Refresher

## Indexing Basics
```python
s = "HELLO"
s[0]  # 'H'
s[-1] # 'O'
```

---

## The WACKY Part (Slices)
```python
s = "PYTHON"
s[0:4]   # 'PYTH'
s[::2]   # 'PTO'
s[::-1]  # 'NOHTYP'
```

---

## Nested Indexing
```python
words = ["CMPT", "Python", ["Wacky", "Indexing"]]
words[2][1]
# 'Indexing'
```

---

# 3. File Reading in Python

## Opening Files
```python
with open("data.txt", "r") as f:
    text = f.read()
```

---

## `.read()` vs `.readline()` vs `.readlines()`
- `f.read()` → whole file as a single string.
- `f.readline()` → one line at a time.
- `f.readlines()` → list of all lines.

---

## Iterating Over a File
```python
with open("data.txt", "r") as f:
    for line in f:
        print(line.strip())
```

---

# 4. Recommendation Systems

## Basic Recommendation
- **Most Popular**: Suggest the most common item.
- Examples: most read news story, most bought product.

---

## Advanced Recommendation
- **People Like You Also Liked**:
    - Andrea likes apples, bananas, cherries.
    - Bob likes durian, bananas, cherries.
    - Suggest Andrea try durian; Bob try apples.

---

## Similarity Scores
- Compare users by overlap in preferences.
- Algorithm:
  1. Initialize top score = 0, top person = "".
  2. For each person:
     - Calculate similarity with you.
     - If higher than top score → update.
  3. At end, top person = most similar.

---

## Activity
Find the person in your dataset who has the **highest similarity score** to you.

---

# 5. Comparisons & Logical Operators (refresher)

## Comparison Operators
- `==` equal  
- `!=` not equal  
- `<`, `<=`, `>`, `>=`

---

## Logical Operators
- `and`: both conditions true (strict)
- `or`: at least one true (not strict)
- `not`: negates condition ("flip" True to False)

---

# 6. Practice Review Questions

## Indexing
```python
singers = ["elsa", "anna", "snowman"]
print(singers[2])   # ?
```

---

## Negative Indexing
```python
favourites = ["roti", "pita", "sourdough", "tortilla"]
print(favourites[-2])  # ?
```

---

## Sublist Slices
```python
letters = ['a', 'b', 'c', 'd', 'e', 'f']
print(letters[1:3])  # ?
print(letters[:4])   # ?
print(letters[3:])   # ?
print(letters[-1])   # ?
```

---

## Nested Loops
What does it mean to have a **nested loop**?  
- Write a quick example.

---

# 7. Live Coding Scaffold

## Activity Prompt 1
- Open a text file.  
- Read its contents.  
- Split text into words.  

---

## Activity Prompt 2
- Create a list of numbers.  
- Demonstrate at least 3 slice operations.  

---

## Activity Prompt 3
- Take a sentence as input.  
- Split into words, reverse order, join back.  

---

# 8. References

- [Runestone Academy: Working with Data Files](http://interactivepython.org/runestone/static/thinkcspy/Files/intro-WorkingwithDataFiles.html)  
- [Runestone Academy: Lists and Strings](http://interactivepython.org/runestone/static/thinkcspy/Lists/StringsandLists.html)  
- [StackOverflow: Difference between read, readline, readlines](https://stackoverflow.com/questions/58073162/difference-in-read-readline-and-readlines-in-python)  
- [Runestone Academy: Logical Operators](http://interactivepython.org/runestone/static/thinkcspy/Selection/Logicaloperators.html)  
