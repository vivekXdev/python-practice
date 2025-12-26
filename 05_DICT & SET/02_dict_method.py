marks = {
    "aman" :67,
    "sagar":87,
    "rohan":54,

    34:"ram"
}


#item
# print(marks.items())    #display all items

# print(marks.keys())         #display all keys
# print(marks.values())       #display all value

# print(marks.get("rohan"))      #get rohan marks

marks.update({"aman":100})    #update aman's marks

print(marks)


marks.pop("sagar")              #delet sagar
print(marks)

marks.clear()               #remove all items

marks.update({"aaa":00})    #update aman's marks
print(marks)

marks.update({"new year" :2026})      #add new pairs

marks.popitem()                     #remove last inserted key-value pair
print(marks)