#the break statement
for i in range(30):
    if(i == 15):
        continue      #skip this iteration (15)
    print(i)        #display 0 to 29 with skip 15


l = ["aman",12,"sagar",34,0,122,"sagar",343]

for s in l:
    if s == "sagar":        #print list without sagar
        continue
    print(s)

