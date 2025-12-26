#WAP to find greatest of three number using function

def greatest(x,y,z):
    if(x>y and x>z):
        return x
    elif(y>x and y>z):
        return y
    else:
        return z



x = 5
y = 6
z = 9



print(f"the gretest number is {greatest(x,y,z)}")