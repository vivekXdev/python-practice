#WA function to print first n lines of the following pattern.
#   ***
#   **
#   *

def p(n):
    if (n == 0):
        return
    print("*"*n)
    p(n-1)

print(p(6))