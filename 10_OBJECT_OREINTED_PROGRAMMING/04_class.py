class Data():
    friut = "pine apple"
    car = "swift"


d = Data()
# d.friut = "apple"
# d.car = "bmw"
d.laptop = "asus"           #laptop is instance(object) attribute
print(d.friut,d.car,d.laptop)       #car and friut is class attribut

d2 = Data()
d2.friut = "banana"
d2.car = "ferari"
print(d2.car,d2.friut)