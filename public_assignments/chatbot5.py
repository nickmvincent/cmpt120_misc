# Program: Keyword Detector
# Name: A. Learner
# Date: 2025-09-10

msg = input("Tell me something? ").strip()
if "hello" in msg.lower():
    print("I heard a greeting!")
elif "bye" in msg.lower():
    print("Goodbye!")
else:
    print("Okay.")
print("bye" in msg.lower())  # Boolean-ish result printed? (prints True/False)
