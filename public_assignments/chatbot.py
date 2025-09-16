# Program: Full-Feature Character Chatbot
# Name: A. Learner
# Date: 2025-09-10
# Pseudocode:
# - Greet
# - Ask 3+ questions
# - Use input saved/unsaved
# - Use string methods, in, loops, nested if, and/or, comparisons
# - Use random.choice on a list of strings

import random

greet = "Hello"
print(greet)  # print a string var
name = input("What's your name? ").strip()
print("Nice to meet you, " + name + "!")  # concatenation

colors = ["blue", "green", "red", "purple"]  # list of strings
print("Random color pick:", random.choice(colors))  # random.choice with import

mood = input("How are you feeling today? ").strip().lower()  # saved
print(input("What should I call you today? "))  # unsaved input call

if "good" in mood or "great" in mood:  # 'in' + 'or'
    print("Yay!")
    fav = input("Favorite color? ").strip().lower()
    if fav == "blue":                 # nested if + comparison
        print(True)                   # print a Boolean literal
    elif fav == "red":
        print("Fiery!")
    elif fav == "green":
        print("Chill.")
    else:
        print("Nice choice!")
else:
    print("Hope things improve.")
    pet = input("Cat or dog? ").strip().lower()
    if pet == "cat" and ("a" in pet):  # 'and' + in + comparison
        print("Meow crew.")
    elif pet == "dog":
        print("Woof pack.")
    elif pet == "parrot":
        print("Talkative friend.")
    else:
        print("All animals are cool.")

# Extra for loop to satisfy loop requirement
for i in range(3):
    print("Loop idx:", i)
