#from a file containing numbers saparated by comma, print the count of even numbers.
with open("demo.txt" , "r") as f:
    a = f.read().replace("," , "").split()
    count = 0
    for i in a:
        if(int(i) % 2 == 0):
            count += 1
    print(count)