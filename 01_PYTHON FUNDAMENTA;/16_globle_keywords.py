#If you use the global keyword, the variable belongs to the global scope:
def myfunc():
    global x
    x = "python"

myfunc()

print("I am Learning " + x)

#To change the value of a global variable inside a function, refer to the variable by using the global keyword:
x = "good"

def myfunc():
    global x
    x = "best"

myfunc()

print("python is "+ x)
