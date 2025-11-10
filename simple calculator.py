a=int(input("enter the 1st number :"))
b=int(input("enter the 2nd number :"))
choice=input("enter your choice +,-,*,/")

if choice =="-":
    print(a-b)
elif choice=="+":
    print(a+b)
elif choice=="*":
    print(a*b)
elif choice=="/":
    print(a/b)
else:
    print("invalid choice")

