L=[]
def signup():
    em=input("Enter email id: ")
    p=input("Enter the password: ")
    a={"Email":em,"Password":p}
    L.append(a)
    print(L)
    signup()
print("Signed up successfully")
def signin():
    em=input("Enter email id:")
    p=input("Enter password:")
    for user in L:
        if user["email"]==em and user["password"]==p:
            print("Signin successfully")
            return
    print("invalid credentials")
while True:
    print("\n1.Signup\n2.signin\n3.Exit")
    choice=input("Enter your choice")
    if choice=="1":
        signup()
    elif choice=="2":
        signin()
    elif choice=="3":
        print("exiting..")
        break
    else:
        Print("invalid choice, try again")