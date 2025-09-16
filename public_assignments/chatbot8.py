# Program: Mood Bot
# Name: A. Learner
# Date: 2025-09-10

import random
moods = ["happy", "sad", "excited", "bored"]
print("Mood of the day:", random.choice(moods))
m = input("How are you? ").strip().lower()
if "great" in m:
    print("Awesome!")
elif "ok" in m:
    print("Got it.")
elif "bad" in m:
    print("Sorry to hear that.")
else:
    print("Thanks for sharing.")
