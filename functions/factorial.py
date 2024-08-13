# method 1:
# def factorial():
#     number = int(input("enter the number to find its factorial"))
#     fact = 1
#     while(number>=1):
#         fact*=number
#         number-=1
#     print(fact)
# factorial()


# method 2:
# num = int(input("enter the number to find its factorial"))
# def factorial(number):
#     fact = 1
#     while(number>=1):
#         fact*=number
#         number-=1
#     print(fact)
# factorial(num)

# method3:
num = int(input("enter the number to find its factorial"))
def factorial(number):
    fact = 1
    while(number>=1):
        fact*=number
        number-=1
    return fact
print(factorial(num))

