# number = int(input("enter the number"))
def is_prime():
    number = int(input("enter the number"))
    is_divisble = False
    for i in range(2,number):
        if(number%i == 0):
            is_divisble = True
            break
        else:
            is_divisble = False
    if(is_divisble):
        print("number is not prime")
    else:
        print("number is prime")
is_prime()