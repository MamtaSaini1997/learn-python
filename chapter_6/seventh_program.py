#write a recursive function to calculate the sum of first n natural numbers:
def sum(n):
    if (n == 0):
        return 0
    else:
       return n + sum(n-1)

print(sum(3))
print(sum(6))