# CAF which calcultes the total count of 1 occur in the range from 1 to 100:
count = 0
for i in range(1, 101):
    for x in str(i):
        if (x == "1"):
            count += 1

x = 0
def a(num):
    global x
    if (num == 0):
        return
    
    for i in str(num):
        if i == "1":
            x += 1
    a(num - 1)

a(100)