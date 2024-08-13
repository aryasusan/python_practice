# numbers from 1 to the entered upper limit
upper = int(input("Enter the upper limit"))
if(upper>=1):
    for i in range(1,upper+1):
        print(i)
else:
    for i in range(1,upper-1,-1):
        print(i)