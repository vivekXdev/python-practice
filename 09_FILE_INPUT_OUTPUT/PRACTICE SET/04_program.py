# A file contains a word “donkey” multiple times. You need to write a program which replace this word with ##### by updating the same file.

word = "donkey"
with open("file4.txt","r") as f:
    content = f.read()

contentnew = content.replace(word,"######")

with open("file4.txt","w") as f:
    f.write(contentnew)