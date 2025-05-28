#search for a number x in this tuple using for loop:
tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
i = int(input("enter number: "))
idx = 0
for j in tup:
    if(i == j):
        print("found at", idx)
        break
    idx += 1