#WAP to creat a span detecter which use to detect following keywords
#--Make a lot of money,buy now,subscribe this,click this,

x = str(input("Write a comment :"))
y = x.lower()

if("make a lot of money" in y):
    print("spam")
elif("buy now" in y):
    print("spam")
elif("subscribe this" in y):
    print("spam")
elif("click this" in y):
    print("spam")
else:
    print("No spam")
