# Write a program to find out the line number where python is present from ques 6.

with open("log.txt","r") as f:
    lines = f.readlines()


line_no = 1
for line in lines:
    if ("python" in line.lower()):
        print(f"python is found at line{line_no}")
        break
    line_no += 1

else:
    print("python is not present")
