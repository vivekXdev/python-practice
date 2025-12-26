#WAP to find whether a name in the list or not
list = ["sandeep","shiva","vinay","suraj","krishika","sangeeta","gunjan","ajeet","karan"]
name = input("Enter your name :")

l = name.lower()

if(l in list):
    print(l,"is in the list")
else:
    print(l,"is not in the list")
