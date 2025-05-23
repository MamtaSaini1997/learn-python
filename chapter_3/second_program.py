#wap to check if a list contains a palindrome of elements.
a = [1, 2, 3, 4, 2, 1]
b = a.copy()
b.reverse()
if(a == b):
    print("yes list is palindrome")
else:
    print("no list is not palindrome")