def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    return a/b
print("Enter 1 to add number.\n Enter 2 to substract.\n Enter 3 to multiply.\n Enter 4 to division.\n")
n=int(input("Enter your choice"))
if(n==1):
    a=int(input("Enter the value of a"))
    b=int(input("Enter the value of b"))
    result=add(a,b)
    print(f" Sum of {a} and {b}={result}")
elif(n==2):
    a=int(input("Enter the value of a"))
    b=int(input("Enter the value of b"))
    result=subtract(a,b)
    print(f" Difference of {a} and {b}={result}")
elif(n==3):
    a=int(input("Enter the value of a"))
    b=int(input("Enter the value of b"))
    result=multiply(a,b)
    print(f" Product of {a} and {b}={result}")
elif(n==4):
    a=int(input("Enter the value of a"))
    b=int(input("Enter the value of b"))
    result=division(a,b)
    print(f" Quotient of {a} and {b}={result}")
else:
    print("Wrong choice")