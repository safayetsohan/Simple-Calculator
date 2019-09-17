a = int(input("First Element:  "))
b = int(input("Second Element: "))

print("1)Add\n2)Sub\n3)Multi\n4)Div\n")

choose = int(input("Please Choose One: "))

if(choose==1):
    print("Result Is: ",(a+b))
elif(choose==2):
    print("Result Is: ",(a-b))
elif(choose==3):
    print("Result Is: ",(a*b))
elif(choose==4):
    print("Result Is: ",a/b)
else:
    exit()