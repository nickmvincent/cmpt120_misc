# Program: Nested Logic
# Name: A. Learner
# Date: 2025-09-10

ans = input("Do you like games? ").strip().lower()
if ans == "yes" or ans == "y":                # or
    genre = input("RPG or FPS? ").strip().upper()
    if genre == "RPG" and "p":  # and (silly but valid)
        print("Role-player detected.")
else:
    print("No worries.")
print(False)
