#there are i have top most using string function

#len()

name = "shishant singh rajput"

print(len(name))    # 21   not consider 0 as a digit

#endswith()

print(name.endswith("put"))     #return true

#startswith()

print(name.startswith("shii"))      #return false


#capitalize()

print(name.capitalize())        #chage first letter of first word in uppercase


#title()

print(name.title())             #change first letter of each word in uppercase


#lower()


print(name.lower())             #change all letters in lower case of string

#upper()


print(name.upper())             #change all letters in lower case of string


#strip()

name2 ="    sagar chaudhary            "
trimed = name2.strip()
print(trimed.strip())             #trim extra space from string only from ind_start and ind_end



#replace

print(trimed.replace("chaudhary","kumar"))          #replace a word into another


#split

marks = "12,13,14"
new_marks = marks.split()
print(new_marks)                        #break string into a list


#join()
stu_age = ['12', '25','37']
print(" ".join(stu_age))                       #jions list into string


#find()

phone ="raj kumar"
print(phone.find("m"))         #find the position of number and alphabet