# create a function which takes a list as an argument and returns the duplicate values from the list

def find_duplicates(list):
    duplicate_value = []
    a = []
    for i in list:
        if (i in a):
            duplicate_value.append(i)
        else:
            a.append(i)
    print(duplicate_value)

find_duplicates([1,4,3,5,6,8,2,4,0,5])