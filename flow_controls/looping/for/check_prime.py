num = int(input("Enter the number"))
is_divisible = False
for i in range(2,num):
    if(num%i == 0):
        is_divisible = True
if(is_divisible):
    print("Number is not prime")
else:
    print("Number is prime")