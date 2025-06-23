# wap to create a new file "practice.txt" using python. Add the following data in it.

# hi everyone
# we are learning file I/O
# using java.
# i like programming in java.

# waf to find in which line of the file does the word "learning" occur first.
# print -1 if the word not found.

f = open("practice.txt" , "r")
result = f.readlines()
status = "Not Found"

def find_line():
    global status
    for i in range(len(result)):
        if("Python" in result[i]):
            print(f"exists in line {i + 1}")
            status = "Found"
    else:
        if (status == "Not Found"):
            print("-1")

find_line()

# second way with "while loop"
def find_line_no():
    i = 0
    while i < len(result):
        if ("learning" in result[i]):
            print(f"exists in line {i + 1}")
            status == "found"
        i += 1
    else:
        if(status == "not found"):
            print(-1)
find_line_no()    

# third way with return statement:
def line_no():
    i = 0
    while i < len(result):
        if ("learning" in result[i]):
            print(f"exists in line {i + 1}")
            return
        i += 1
    return -1
print(line_no())
   