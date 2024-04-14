f = open("Demo.txt", "r")

#read first line
# print(f.readline()) 

#read number of character
# print(f.read(15))
count =1
for x in f:
    print(count,x)
    count=count+1
f.close()

#Number of Lines , Number of words 