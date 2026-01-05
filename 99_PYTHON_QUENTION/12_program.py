#Wap to creat a class with instance(object) attributes
class Computer():
    moniter = "dell"
    mouse = "lenovo"
    keyborad = "ant"

pc1 = Computer()
pc1.moniter = "asus"                        #here asus is the instance attribute that change the value of moniter for pc1
print(pc1.moniter,pc1.mouse,pc1.keyborad)