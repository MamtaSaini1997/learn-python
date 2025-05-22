#wap to find the greatest of 3 numbers entered by the user.
a = int(input("enter ist number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))
if(a >= b and a >= c):
    print("a is greatest")
elif(b >= c):
    print("b is greatest")
else:
    print("c is greatest")