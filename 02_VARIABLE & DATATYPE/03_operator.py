# Arithmetics operator + , -, *, /.
a = 34
b = 12

# print(a+ b)
# print(a- b)
# print(a* b)
# print(a/ b)


# Assignment operater  = , += , -=
e = 2-1  

f = 19
f += 1      # adding 3 into f 
# print(f)

g = 45
g -=5       #subtract 5 from 45
#print(g)


#Comparsion operator == , >= , <= , != , 
d = 9>3
#print(d)            #these operator always return boolean  true & false


k = 60<10
#print(k)        

r = 5 == 5
#print(r)

j = 10!=9
#print(j)


#Logical operatore  OR , AND , NOT .

#truth table of OR
print("True or True is ", True or True)
print("True or False is ", True or False)
print("False or True is ", False or True)
print("False or False is ", False or False)

example = (2>3 or 3>2)
print(example)          #true


#truth table of AND
print("True and True is ", True and True)
print("True and False is ", True and False)
print("False and True is ", False and True)
print("False and False is ", False and False)

example2 = (10>9 and 10 < 10)
print(example2)


#NOT

hour = 12
print(not(hour<10))    #NOT change ture into false and false into true



age = 18
print(not(age > 20))