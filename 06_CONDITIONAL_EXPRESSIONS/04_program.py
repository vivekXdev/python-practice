#WAP to find geatest number of the four number entered by the user.
x1 = int(input("Enter number 1 :"))
x2 = int(input("Enter number 2 :"))
x3 = int(input("Enter number 3 :"))
x4 = int(input("Enter number 4 :"))

if(x1>x2 and x1>x3 and x1>x4):
    print(x1,"is greatest")
elif(x2>x1 and x2>x3 and x2>x4):
    print(x2,"is greatest")
elif(x3>x1 and x3>x2 and x3>x4):
    print(x3,"is greatest")
else:
    print(x4,"is greatest")