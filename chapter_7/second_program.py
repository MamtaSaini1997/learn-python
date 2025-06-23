#wap to create a new file "practice.txt" using python. Add the following data in it.
#hi everyone
#we are learning file I/O
#using java.
# i like programming in java.

#waf that replace all occurrences of "Java" with "Python" in above file.
f = open("practice.txt" , "r")
a = f.read().replace("java", "Python")
f.close()
f = open("practice.txt" , "w")
f.write(a)