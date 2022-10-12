#write a program to swap value of two variable without using 3rd variable
num1 = int(input("Enter first number")) #10
num2 = int(input("Enter second number")) #20
print("before swaping",num1,num2)
num1 = num1 + num2 #30
num2 = num1 - num2 #10
num1 = num1 - num2 # 20
print("after swaping ",num1,num2)
