"""
weeks1-3.py
Author: Nicholas Vincent
Date: 2025-09-08
Purpose: A single, top-to-bottom Python file that students can read and run.
         Covers concepts from Weeks 1–3. comments, pseudocode, variables, input/output, strings, 
         lists,
         random, conditionals, and for-loops with range().
"""

# ===== Imports (Week 2: put import statements at the top, after header) =====
import random  # 'random' is a module; modules contain functions. The dot accesses an attribute (like a function).

# ============================================================================
# WEEK 1 — FOUNDATIONS
# ============================================================================

# CS is problem solving. We often decompose problems into smaller subtasks.
# We'll build a tiny, text-based "greeter & list explorer" program step by step.

# Program header block already shown above (author, date, purpose) (Week 1).

# Pseudocode (Week 1: know what pseudocode is):
# 1) Say "Hello World".
# 2) Ask for the user's name, store it in a variable.
# 3) Greet the user using their name.
# 4) Contrast natural vs programming language via a brief printed example.
# 5) Show that we can submit a single .py or bundle in a .zip (comment only).

# Step 1: Hello World (Week 1)
print("Hello World")  # Python comment: explains code without being executed.

# Step 2/3: Input name and greet (Week 2 preview for input + concatenation later)
# (Keep it simple: store terminal input into a variable.)
user_name = input("What is your name? ")  # saved to a variable

# Header block info reminder (Week 1): author, date, brief description is at the top.

# Print a greeting using string concatenation (Week 2 concept):
print("Nice to meet you, " + user_name + "!")

# Natural vs programming languages (Week 1: contrast). This is just text:
print("In natural language, requests can be vague; in code, steps must be explicit.")

# IDLE vs IDE (Week 1):
print("IDLE is simple and comes with Python; IDEs like VS Code add helpful tools.")

# Submitting code (Week 1):
print("Submit as a .py file, or multiple files as a .zip, per your course instructions.")

# Pause without saving the input (Week 2: receive input without saving)
input("(Press Enter to continue...) ")  # value is not saved to any variable

# ============================================================================
# WEEK 2 — INPUTS, VARIABLES, STRINGS, LISTS, RANDOM, BOOLEAN LOGIC, TESTING
# ============================================================================

# Design/plan an algorithm using comments/pseudocode (Week 2):
# Task: Build a random nickname from a list, and respond differently based on color choice.
# Steps:
#   1) Gather a preferred color from the user; normalize it.
#   2) Have a list of possible nicknames; pick one at random.
#   3) Print the nickname.
#   4) Use if/elif/else with == to respond to the color.
#   5) Demonstrate Boolean expressions with comparisons and and/or.

# Variable naming and data types (Week 2): descriptive, lowercase_with_underscores.
preferred_color = input("Pick a color you like (red/green/blue/other): ")
preferred_color = preferred_color.strip().lower()  # also uses Week 3 methods early for better UX

# A list of strings (Week 2):
nicknames = ["ace", "sparky", "nova", "pixel"]

# Use random.choice on a list (Week 2). The dot after a module name accesses its attribute.
random_nickname = random.choice(nicknames)
print("Your random nickname is: " + random_nickname)

# if/elif/else with == (Week 2), plus else clause
if preferred_color == "red":
    print("Red feels bold!")
elif preferred_color == "green":
    print("Green feels calm!")
elif preferred_color == "blue":
    print("Blue feels cool!")
else:
    print("Nice choice!")

# Comparison operators and Boolean expressions (Week 2)
# We'll create a small integer and test conditions. You can see True/False results.
number = 5  # Integer type (Week 3 will discuss more)
print("Is number > 3 and < 10?", (number > 3) and (number < 10))
print("Is number == 0 or == 5?", (number == 0) or (number == 5))
print("Print a Boolean expression directly:", (preferred_color == "red"))

# Basics of combining Boolean expressions using and/or (Week 2)
print("Is color 'red' or 'blue'?", (preferred_color == "red") or (preferred_color == "blue"))

# Short program description belongs in header (done). Interpreter catches syntax errors
# before running; runtime errors happen during execution (Week 2 note). We keep the
# code simple and interactive so you can test normal and unexpected inputs.

# Commenting out blocks to test smaller pieces (Week 2):
# Try uncommenting the next line to test only a tiny piece during your own experiments.
# print("(Testing small piece)")

# ============================================================================
# WEEK 3 — STRINGS, LISTS, LOOPS, RANGE, TYPES, NESTED CONDITIONALS
# ============================================================================

# String methods: strip, lower, upper (Week 3)
raw_word = input("Type a messy word (e.g., '  PyThOn  '): ")
print("strip:", raw_word.strip())
print("lower:", raw_word.lower())
print("upper:", raw_word.upper())

# Identify the String data type (Week 3)
print("type(raw_word):", type(raw_word))

# Method chaining (Week 3):
print("chained strip+lower:", raw_word.strip().lower())

# 'in' keyword for lists and strings (Week 3)
print("Is 'ace' in nicknames?", "ace" in nicknames)
print("Is 'na' in 'banana'?", "na" in "banana")

# Create a list using variables from user input (Week 3)
count_str = input("How many favorite foods will you enter? ")
# Convert to Integer (Week 3):
count = int(count_str)  # concatenation is only between strings; we convert when needed

foods = []  # a list of strings

# Use a for-loop with range() and an index variable i (Week 3)
for i in range(count):  # i will be 0,1,2,...,count-1
    food = input("Enter food " + str(i + 1) + ": ").strip()
    foods.append(food)

# Loop over elements of a list (Week 3)
print("You entered:")
for food in foods:
    print("- " + food)

# Show Integer-to-String conversion for concatenation (Week 3)
answer_num = 42
print("Answer=" + str(answer_num))  # cannot concatenate int directly; convert to str

# Design and implement nested conditionals (Week 3) with simple robustness
score_str = input("Enter a score from 0 to 100: ")
# Light robustness: check content before converting (still only using covered ideas)
# We will treat non-digits as unexpected input and skip grading.
all_digits = True
for ch in score_str:
    if not ("0" <= ch <= "9"):
        all_digits = False

if all_digits and (score_str != ""):
    score = int(score_str)
    if 0 <= score <= 100:
        # nested conditionals
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "F"
        print("Grade: " + grade)
    else:
        print("Semantic error example: a value outside 0–100 doesn't make sense for a score.")
else:
    print("Unexpected input (not a non-negative integer). Try again next run.")

# Syntax vs semantic errors (Week 3):
# - Syntax error: e.g., removing a quote would prevent the program from starting.
# - Semantic error: e.g., logically invalid score like 500 still runs but is incorrect.

# Robustness (Week 3): we gently handled non-digit input above using only simple checks.

# Range reminder (Week 3): shows the numbers 0..2
for i in range(3):
    print("range example i=", i)

# END — You've just read and executed a single-file program that touches every
# listed outcome from Weeks 1–3, using only the covered concepts.
