num1 = int(input("Enter num1"))
num2 = int(input("Enter num2"))
num3 = int(input("Enter num3"))
if((num1>num2) & (num1>num3)):
    print(num1,"is largest")
elif((num2>num1) & (num2>num3)):
    print(num2, "is largest")
else:
    print((num3,"is largest"))