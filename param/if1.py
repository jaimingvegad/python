#write a program to findout findout qube of given positive number 
number = int(input("enter number to findout it's qube")) # -10
if number<0: #< > <= >= == != (relational operators)
    number = 0 - number
    print("number is converted into positive number")
qube = number * number * number #samikaran 
print("qube is ",qube)