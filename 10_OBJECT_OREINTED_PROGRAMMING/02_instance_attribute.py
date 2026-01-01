#Example 1
class student:
    batch = "3pm"
    course = "dafa"
    fee = 8500


aman = student()
aman.course = "dwd"                    #hers course is instance attribute thats chage the value of course in student class
print(aman.batch,aman.course,aman.fee)          

#Example 2
class Student:
    course = "BCA"
    fees = 45000


Student.cgpa = 8                    #new added instance(object) attribut
Student.course = "BCOM"             #
print(Student.course,Student.cgpa,Student.fees)

