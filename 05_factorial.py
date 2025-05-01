# program to print the factorial of given number


num=int(input("Please enter a number:"))

factorial=1

if num<0:
    print("Factorial of negative number does not exist.")

if num==0:
    print("Factorial of 0 = 1")


else:
    for i in range(1, num + 1):
        factorial *= i
        print("Factorial of",num,"=",factorial)
    