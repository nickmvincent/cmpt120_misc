
def cleaner_binary_to_decimal(x):
    ret = 0
    power = 0
    for i in range(len(x)-1, -1, -1):
        print("i is ", i)
        # here we grab the 0 or 1 from the binary string at index i (recall that i counts down from 
        # right to left, so in this example is goes 3,2,1,0
        # it's a string that's passed here, so we need to convert it to an integer,
        val_as_int = int(x[i])
        if val_as_int:
            print(f"current power val is {power} and 2 to this power is {2**power}")
            print("we add this because the binary string has a 1 in this place")
            ret += 2**power
        power +=1
    return ret


while True:
    print("hello user, give me a binary string")

    binary_string_from_user = input()

    if binary_string_from_user.lower() == "q":
        break

    error_found = False
    for char in binary_string_from_user:
        if char not in ["0", "1"]:
            print("there is a character in your string that is not 0 or 1")
            error_found = True
    if error_found:
        continue
    print("here is your binary string as a decimal")
    val = cleaner_binary_to_decimal(binary_string_from_user)
    print(val)

    print("ok here we go again..")
