#wap to find the factorial of first n natural numbers(using for loop):
n = int(input("enter number: "))
fact = 1
for i in range(1 , (n + 1)):
    fact *= i
print("factorial is: ", fact)