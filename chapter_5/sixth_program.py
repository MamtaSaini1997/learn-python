#search for a number x in this tuple using loop:
a  = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
c = 0
i = int(input("enter number: "))
while len(a) != c:
   print(a[c] == i)
   c += 1


#second method:
b  = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
j = 0
x = int(input("enter number: "))

while j < len(b):
    if b[j] == x:
        print("found")
    else:
        print("finding..")
    j += 1