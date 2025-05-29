#waf to return odd or even string as according to number is given:
def tell_type(n):
    n = int(input("enter number: "))
    if (n % 2 == 0):
        print(str("even"))
    else:
        print(str("odd"))

tell_type(5)
tell_type(6)           