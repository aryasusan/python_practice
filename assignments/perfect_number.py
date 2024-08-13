# perfect number is a number which is equal to the sum of
# its divisors excluding itsef:
# eg: 6 divisors:1,2,3    1+2+3=6

num = int(input("Enter the number to check if its a perfect num:"))
sum = 1
for i in range(2,num):
    if(num%i==0):
        sum+=i
if(sum==num):
    print("Perfect number")
else:
    print("Not perfect number")