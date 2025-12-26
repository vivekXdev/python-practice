#WAP to calculate the grade of a student from his marks
#90-100 - Excelent
#80-90  - A
#70-80  - B
#60-70  - C
#50-60  - D
#<50   - fail

marks = int(input("Enter your marks:"))
if(marks> 100):
    print("you enterd invaild marks")
elif(marks <= 100 and marks>=90):
    print("Excelent")
elif(marks <= 90 and marks>=80):
    print("grade A")
elif(marks<=80 and marks>=70):
    print("grade b")
elif(marks<=70 and marks>=60):
    print("grade c")
elif(marks<=60 and marks>=50):
    print("grade d")
else:
    print("fail")