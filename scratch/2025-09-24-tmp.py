# ===
# coffee recsys
# ===

starbucks_count = 0
tims_count = 0

num_iterations = 20
for i in range(num_iterations):
    print("tell me ur fav coffee: either S/s or T/t")
    choice = input()
    while choice.lower() not in ["s", "t"]:
        print("try again, do S/s, or T/t")
        choice = input()
    choice_l = choice.lower()
    if choice_l == "s":
        starbucks_count += 1
    elif choice_l == "t":
        tims_count += 1


starbucks_count = 5
tims_count = 7
num_iterations = 12
        
print(f"Starbucks count was {starbucks_count} and Tims count was {tims_count}")
starbucks_frac = starbucks_count / (num_iterations)
print("{:.2f}".format(starbucks_frac))
starbucks_percent = starbucks_count / num_iterations * 100
print(starbucks_percent)


mydata = [
        # 0.         1.                         2
    ["player1", "scoring_from_last_night_game", 25],
    ["player2", "scoring_from_last_night_game", 17],
]

sum_of_all_scores = 0
max_score = 0
for row in mydata:
    print(row)
    sum_of_all_scores += row[2]
    if row[2] > max_score:
        max_score = row[2]

print(sum_of_all_scores)
print(max_score)
