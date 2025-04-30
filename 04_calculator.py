#Simple calculator

num1=float(input("Enter first number"))
num2=float(input("Enter second number"))

print("Please choose the operation")
print("+ = addition")
print("- = subtraction")
print("* = multiplication")
print("/ = division")
print("% = modulus")

#taking the operation input from the user
choice=input("please select the operation")
num1
if choice=="+":
    print("addition of ",num1 ,"and",num2, "=",num1+num2)
elif choice=="-":
    print("subtraction of ",num1 ,"and",num2 ,"=",num1-num2)
elif choice=="*":
    print("multiplication of ",num1, "and",num2 ,"=",num1*num2)
elif choice=="/":
    print("division of ",num1 ,"and",num2 ,"=",num1/num2)
elif choice=="%":
    print("modulus of ",num1, "and",num2, "=",num1%num2)
else:
    print("invalid operation")
