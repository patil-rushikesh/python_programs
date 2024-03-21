import os
#Creating
#f = open("myfile.txt", "x")
#opening
f = open("myfile.txt", "r")
print(f.read())
f.close()
print("created File\n")
#appending
f = open("myfile.txt", "a")
f.write("This is first line")
f.close()
print("written in a file\n")
#opening
f = open("myfile.txt", "r")
print(f.read(),"\n")
f.close()
#overwrite
f = open("myfile.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()
#opening
f = open("myfile.txt", "r")
print(f.read(),"\n")
f.close()

#deleting
os.remove("myfile.txt")

f = open("myfile.txt", "r")
print(f.read(),"\n")
f.close()
