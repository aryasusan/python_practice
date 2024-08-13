lower = int(input("enter the lower limit"))
upper = int(input("enter the upper limit"))
is_divisible = False
for i in range(lower,upper+1):
    for j in range(2,i):
        if(i%j == 0):
            is_divisible = True
            break
        else:
            is_divisible = False
    if(is_divisible):
        pass
    else:
        print(i)