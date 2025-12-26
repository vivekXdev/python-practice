#WAP to using function to convert celsius to fahrenheit

#c/5 = (f-32)/9   

# def c_to_f(c):
#     return ((c +32)/5)*9


# c = int(input("Enter temperatur in c:"))
# f = c_to_f(c)
# print(f"{round(f,2)}f")

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)

print("Fahrenheit =", fahrenheit)
 