# write a programe to print 2 digit number in word
# --> 26 = two six
# --> 78 = seven eight
number=int(input("Enter your number "))
print("the value of number is ",number)

if number>9 and number<99:
    first =  int(number/10)
    second = number%10
    print("the value of first is ",first,"the value of second is ",second)
    if first==1:
        print("One")
    elif first==2:
        print("Two")
    elif first==3:
        print("Three")
    elif first==4:
        print("four")
    elif first==5:
        print("five")
    elif first==6:
        print("six")
    elif first==7:
        print("seven")
    elif first==8:
        print("eight")
    elif first==9:
        print("nine")
    elif first==0:
        print("zero")

    if second==1:
        print("One")
    elif second==2:
        print("Two")
    elif second==3:
        print("three")
    elif second==4:
        print("four")
    elif second==5:
        print("five")
    elif second==6:
        print("six")
    elif second==7:
        print("seven")
    elif second==8:
        print("Eight")
    elif second==9:
        print("nine")
    elif second==0:
        print("Zero")
else:
    print("invalid number")