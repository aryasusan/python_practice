num1 = 10
num2 = 20
print("before swapping number1 is", num1, "and number2 is", num2)

# WITH TEMPORARY VARIABLE
temp = num1   # temp= 10
num1 = num2   # num1= 20
num2 = temp   # num2= 10
print("after swapping number1 is", num1, "and number2 is", num2)

#WITHOUT A VARIABLE
num1 = 10
num2 = 20
num1 = num2+num1  # num1 =10+20 = 30
num2 = num1-num2  # num2 =30-20 = 10
num1 = num1-num2  # num1 =30-10 = 20
print("after swapping number1 is", num1, "and number2 is", num2)

#SINGLE LINE SWAPPING
num1 = 10
num2 = 20
a,b,c,d = 10,20,30,40
print(a)
print(b)
print(c)
print(d)
num1, num2 = num2, num1
print("after swapping number1 is", num1, "and number2 is", num2)

