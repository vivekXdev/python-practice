#WAP a recursive funtion to calculate the sum of first n natural numebers.

def sum(n): 
    if n == 1:
        return 1
    return sum(n-1)+n



n = int(input("Enter the number :"))
print(sum(n))
