#write a recursive function to print all elements in a list.(use list and index as parameter):
def print_elements(idx = 0, x = [1,2,3,4,5]):
    if (len(x) == idx):
        return 0
    print(x[idx])
    print_elements(idx + 1)

print_elements()