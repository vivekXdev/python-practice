#WAP to find out whether a student has passed or failed if it required total percentgae 40% and 33% marks in each subject
hindi = int(input("Enter hindi marks :"))
eng = int(input("Enter eng marks :"))
math = int(input("Enter math marks :"))
science = int(input("Enter science marks :"))
sst = int(input("Enter sst marks :"))

# if((hindi/100)*100 < 33):
#     print("you are failed")
# elif((eng/100)*100 < 33):
#     print("you are failed")
# elif((math/100)*100 < 33):
#     print("you are failed")
# elif((sst/100)*100 < 33):
#     print("you are failed")
# elif((science/100)*100 < 33):
#     print("you are failed")
# elif((hindi+eng+math+sst+science)/500*100 < 40 ):
#     print("you are failed")
# else:
#     print("You are passed")

#alternative program for this
total_per = (hindi+eng+math+sst+science)/500*100

if(total_per >=40 and hindi>=33 and eng>=33 and math>=33 and sst>=33 and science>=33):
    print("you are pass",total_per)
else:
    print("You are fail")