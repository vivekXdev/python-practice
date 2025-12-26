#SORT 
a = [1,5,3,5,7,76.00,45.777]
a.sort()                        #[1, 3, 5, 5, 7, 45.777, 76.0]
print(a)


#REVERSE
a.reverse()                     #[76.0, 45.777, 7, 5, 5, 3, 1]

print(a)


#APPEND
a.append("manoj")               #[76.0, 45.777, 7, 5, 5, 3, 1, 'manoj']
print(a)


#insert
a.insert(5,"hello")
print(a)                        #[76.0, 45.777, 7, 5, 5, 'hello', 3, 1, 'manoj']


#pop    :delete a obj from its index
a.pop(5)
print(a)                        #[76.0, 45.777, 7, 5, 5, 3, 1, 'manoj']


#remove      :remove a particulare obj
a.remove("manoj")               
print(a)                        #[76.0, 45.777, 7, 5, 5, 3, 1]



