"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""
num = [4, 6, 3, 9, 1]
t = 5
x = 0
y = 1
while y < len(num):
    if((num[x] + num[y]) == t):
        print([x , y])    
    y += 1