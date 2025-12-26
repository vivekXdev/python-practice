marks = int(input("Enter your marks :"))

if(marks>=33):
    print("You are pass")

if(marks>=60):
    print("You got grade a")
elif(marks>=40):
    print("You got grade b")
elif(marks>=33):
    print("You got grade c")
else:
    print("You are fail")