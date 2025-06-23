#wap to create a new file "practice.txt" using python. Add the following data in it.
#hi everyone
#we are learning file I/O
#using java.
# i like programming in java.
#wap to search if the word "learning" exists in the file or not.

f = open("practice.txt" , "r")
a = f.read()
if("learning" in a):
    print("exists")
else:
    print("not exists")

# second way
if(a.find("learning") != -1):
    print("exists")
else:
    print("not exists")
