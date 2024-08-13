def sum(num1,num2):
    sum = 0
    sum = num1+num2
    return sum
def difference(num1,num2):
    diff = 0
    diff = num1-num2
    return diff
def product(num1,num2):
    prod = 1
    prod = num1*num2
    return prod
def division(num1,num2):
    quotient = num1/num2
    return quotient


num1 = int(input("Enter number 1"))
num2 = int(input("Enter number 2"))
choice = int(input("Enter the choice"))

if(choice==1):
    print("sum is ",sum(num1,num2))
elif(choice == 2):
    print("difference is ",difference(num1,num2))
elif(choice==3):
    print("product is ",product(num1,num2))
elif(choice==4):
    print("quotient is ",division(num1,num2))
else:
    print("Invalid choice")
print("1.Addition",sum(num1,num2),"\n","2.Subtraction",difference(num1,num2),"\n","3.Multiplication",product(num1,num2),"\n","4.Division",division(num1,num2))