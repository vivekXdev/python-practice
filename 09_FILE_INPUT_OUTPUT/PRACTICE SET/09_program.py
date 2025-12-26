# Write a program to find out whether a file is identical & matches the content of another file.

with open("this.txt") as f:
    cont1 = f.read()

with open("this_copy.txt") as f:
    cont2 = f.read()

if cont1 == cont2:
    print("yes thse file are identical")
else:
    print("file are not identical")