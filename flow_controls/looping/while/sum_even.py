upper_limit = int(input("Enter the upper limit"))
lower_limit = int(input("Enter the lower limit"))
sum = 0
while(lower_limit<=upper_limit):
    if(lower_limit%2 == 0):
        sum+=lower_limit
    lower_limit+=1
print(sum)