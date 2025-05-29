#waf to find the factorial of n.(n is the paramater):
def fact(n):
    f = 1
    for i in range(1 , (n + 1)):
        f *= i
    print("factorial is:", f)
       
n = 5
fact(n)   

m = 6
fact(m)

fact(7)