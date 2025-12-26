#display this patters
''' ***
    * *           for = 3
    ***'''
n = int(input("Enter the number :"))
for i in range(1,n+1):
    if i == 1 or i == n:
        print("*"*n)
    else:
        # print("*"+" "*(n-2)+"*")
        print("*",end="")
        print(" "*(n-2),end="")
        print("*")