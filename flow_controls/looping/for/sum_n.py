# sum of numbers from entered lowered limit to the entered upper limit

lower = int(input("Enter the lower limit"))
upper = int(input("Enter the upper limit"))

sum = 0
for i in range(lower,upper+1):
    sum+=i
print(sum)