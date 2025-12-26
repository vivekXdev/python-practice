f = open("file.txt")

#read file using while loop
line = f.readline()
while line != "":
    print(line)
    line = f.readline()