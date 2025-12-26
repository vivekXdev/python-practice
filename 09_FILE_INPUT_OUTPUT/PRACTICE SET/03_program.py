# Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder for a 13 – year old.
def generattable(n):
    table = ""
    for i in range(1,11):
        table += f"{n} X {i} = {n*i}\n"
    
    with open(f"TABLE 2 TO 20/table_{n}.txt","w") as t:
        t.write(table)


for i in range(2,20):
    generattable(i)