#write a program to findout area of 3 shape using given length and width of each. and findout which shape is largest.
length1 = int(input("Enter length of 1st shape"))
width1 = int(input("Enter width of 1st shape"))

length2 = int(input("Enter length of 2nd shape"))
width2 = int(input("Enter width of 2nd shape"))

length3 = int(input("Enter length of 3rd shape"))
width3 = int(input("Enter width of 3rd shape"))

area1 = length1 * width1
area2 = length2 * width2
area3 = length3 * width3

print("area 1",area1,"area 2",area2,"area 3",area3)
if area1>area2: #outer decision making
    if area1>area3: #inner decision making 
        print("first shape is the largest shape")
    else:
        print("third shape is the largest shape")
else:
    if area2>area3:
        print("second shape is the largest shape")
    else:
        print("third shape is the largest shape")