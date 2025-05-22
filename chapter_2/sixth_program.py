#wap to find the greatest of 43 numbers entered by the user.
a = int(input("enter ist number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))
d = int(input("enter fourth number: "))
if(a >= b and a >= c and a >= d):
    print("a is greatest")
elif(b >= c and b >= d):
    print("b is greatest")
elif(c >= d):
    print("c is greatest")
else:
    print("d is greatest")