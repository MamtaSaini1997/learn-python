#figure out a way to store 9 & 9.0 as separate values in the set.
#first way
values = {str(9), 9.0}
print(values)


#second way
values = {9, "9.0"}
print(values)

#third way
values = {
    ("int", 9),
    ("float", 9.0)
}
print(values)