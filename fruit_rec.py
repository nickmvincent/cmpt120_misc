with open("data.csv", "r") as f:
    all_lines = f.readlines()
    header = all_lines[0]
    content_lines = all_lines[1:]
    print(f"The header is {header.strip().split(',')}")
    # print(content_lines)
    cleaned_content_lines = []
    for line in content_lines:
        cleaned_content_lines += [line.strip().split(",")]
    for line in cleaned_content_lines:
        print(line)
        print(" **. ")

cleaned_content_lines # this is where the gold is

# dict_that_maps_person_to_winner = {}


target = "Alice"
alice_row = cleaned_content_lines[1]

max_score = 0
winner_name = ""
for row_we_are_checking_right_now in cleaned_content_lines:
    name = row_we_are_checking_right_now[0]
    if name == "Alice":
        continue

    score = 0
    # we're hand-selecting columns from data.csv
    # we're skipping a specific column, durian, in column 5 / index 4
    for index in [1,2,3,5,6,7,8]:
        if alice_row[index] == row_we_are_checking_right_now[index]:
            score += 1
    print(name, score)
    if score > max_score:
        print("setting max")
        max_score = score
        winner_name = name

print(f"Max score was {max_score}, winner was {winner_name}")