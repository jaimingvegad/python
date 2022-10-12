# write a programe to findout which office is lower out of given three offices accept height and width of office from user
height1=int(input("Enter height of office 1 "))
width1=int(input("Enter width of office 1 "))
height2=int(input("Enter height of office 2 "))
width2=int(input("Enter width of office 2 "))
height3=int(input("Enter height of office 3 "))
width3=int(input("Enter width of office 3 "))
area1=height1*width1
area2=height2*width2
area3=height3*width3
if area1 < area2:
    if area1 < area3:
        print("the area of office 1 is lowest ")
    else:
        print("the area of office 3 is lowest ")
else:
    if area2 < area3:
        print("the area of office 2 is lowest ")
    else:
        print("the area of office 3 is lowest ")