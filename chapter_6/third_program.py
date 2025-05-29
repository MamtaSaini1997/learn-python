#waf to print the elements of a list in a single line.(list is the parameter):
def print_list(list):
    m = len(list)
    i = 0
    while i < m:
        print(list[i], end = " ")
        i += 1

list = [1, 2, 3, 4, 5, 6]        
print_list(list)   
week_days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
print_list(week_days)


#second_way
def print_list(list):
    for i in list:
        print(i, end = " ")

list = [1, 2, 3, 4, 5, 6]        
print_list(list)

week_days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
print_list(week_days)