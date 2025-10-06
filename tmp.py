mylist = [120, 6, 10]

total = 0
for num in mylist:
    total += num
avg = total / len(mylist)
print(f"{avg:.2f} is the avg to 2 decimal places")
print("{:.2f} is the avg to 2 decimal places".format(avg))

myoutput = ""
myoutput += f"{avg:.2f}"
myoutput += " is the avg to 2 decimal places"
print(myoutput)

