#wap to find the sum of first n natural numbers using while loop:
n = int(input("enter number: "))
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print("Sum is:", sum)