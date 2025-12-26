#Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’.
f = open("poem.txt")

data = f.read()

if "twinckle" in data:
    print("twincle found")
else:
    print("twincle not found")


f.close()