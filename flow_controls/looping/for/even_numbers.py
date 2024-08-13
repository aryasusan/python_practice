upper = int(input("Enter the upper limit"))
lower = int(input("Enter the lower limit"))
for i in range(lower,upper+1):
    if(i%2 == 0):
        print(i)