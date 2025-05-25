#wap to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.
a = int(input("enter physics marks : "))
b = int(input("enter chemistry marks: "))
c = int(input("enter math marks: "))
info = {}
new_dict = {"physics" : a,
             "chemistry" : b,
             "math" : c}
info.update(new_dict)
print(info)