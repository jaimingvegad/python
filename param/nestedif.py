# example of nested if else
# write a programe to find greatest number out of given three number 
num1=int(input("Enter any number 1 "))
num2=int(input("Enter any number 2 "))
num3=int(input("Enter any number 3 "))
if num1 > num2:
    if num1 > num3:
        print("the value of num1 is greater than all ")
    else:
        print("the value of num3 is greater than all ")
else:
    if num2 > num3:
        print("the value of num2 is greater than all ")
    else:
        print("the value of num3 is greater than all ")