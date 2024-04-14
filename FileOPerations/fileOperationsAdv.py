#Read throws error if file does not exist
# f = open("Demo123.txt", "r")

#Write will create the file if it does not exist 
# f = open("Demo123.txt", "w")
# f.close()
# f = open("Demo123.txt", "r")
# print(f.read())

#append will create the file if it does not exist 
f = open("Demo1234.txt", "a")
f.close()
f = open("Demo1234.txt", "r")
print(f.read())