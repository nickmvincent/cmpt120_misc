# # us hardcoding data into python

# mylist = [1,2,3]

# for item in mylist:
#     print(item)

# # getting lots of user inputs

# for _ in range(5):
#     val = input()
#     # user might type 5, 3, 1, 0

# # getting data from a file

# open()

# # in your job, get data from a big database

# # mock up of what this might look

# import mycompaniesbigdatalibrary as datalibrary

# data = datalibrary.load_from_database("gooddata")

# user_query = input()

# # user_query is red shoe, blue shoe, or green shirt

# has_red_shoe = data.search(user_query)

# # this might have 5 million rows


# a = 5 # 5 dollar toothpaste
# b = 800 # 800 dollar iphone

# tmp = 5
# a = 800
# b = tmp


def my_constant_time_func(items):
    """
    items is a list of size n, can have any number of items
    """
    return 5


def my_linear_search(items, target):
    """
    items is a list of n items
    `target` is a thing we're looking for
    return True if the target is found
    """
    for item in items:
        if item == target:
            return True
    return False


pretend_dictionary = [
    "apple", # 0
    "banana",# 1 # LOOK HERE SECOND
    "cherry",# 2 # LOOK HERE THIRD
    "durian",# 3
    "eucalyptus", # 4 # LOOK HERE FIRST
    "fruit", # 5
    "g" # 6
    "h", # 7
    "i", # 8
    "j" # 9
]


def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False

    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            # throw away right half
            if item < alist[midpoint]:
                last = midpoint-1
            # throw away left half
            else:
                first = midpoint+1

    return found
	
# 18	testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
# 19	print(binarySearch(testlist, 3))
# 20	print(binarySearch(testlist, 13))


[1,2. ,3,4]

[1,2] [3,4]

[1][2][3][4]