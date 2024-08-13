num1 = int(input("Enter number 1 "))
num2 = int(input("Enter number 2 "))
num3 = int(input("Enter number 3 "))

num4 = (num1, num2, num3)
print(max(num4), "is array")

if (num1>num2) & (num1<num3):
    print(num1, "is 2ndlargest")
elif (num2>num1) & (num2<num3):
    print((num2, "is 2nd largest"))
else:
    print(num3, "is 2nd largest")


##NESTED IF

if (num1>num2) & (num1>num3):
    if(num2>num3):
        print(num2,"is 2nd largest")
    else:
        print(num3, "is 2nd largest")
elif (num2>num1) & (num2>num3):
    if(num1>num3):
        print(num1, "is 2nd largest")
    else:
        print(num3, "is 2nd largest")
else:
    if(num1>num2):
        print(num1, "is 2nd largest")
    else:
        print(num2, "is 2nd largest")
