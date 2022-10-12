# write a programe to find wheter the given number is odd or even
number=int(input("Enter your number "))
print("the value of number is ",number)

if number%2==0:
    print("this is even number ")
elif number%2!=0:
    print("this is odd number ")
else:
    print("this is not even nor odd ")