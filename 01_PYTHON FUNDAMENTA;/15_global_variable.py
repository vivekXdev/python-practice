#Create a variable outside of a function, and use it inside the function
x = "Boy"

def myfunc():
    print("Ram is a " + x)

myfunc()

#output - Ram is a boy

#Create a variable inside a function, with the same name as the global variable
x = "Boy"

def myfunc():
    x = "Man"
    print("Ram is a " + x)

myfunc()

print("Ram is a " + x)

#inside_function_output - Ram is a Man
#outside_function_output - Ram is a Boy
