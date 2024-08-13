upper_limit = int(input("Enter the upper limit"))
lower_limit = int(input("Enter the lower limit"))
sum_even = 0
sum_odd = 0
while(lower_limit<=upper_limit):
    if(lower_limit%2 == 0):
        sum_even+=lower_limit
    else:
        sum_odd +=lower_limit
    lower_limit+=1
print(sum_even,"Even sum")
print(sum_odd,"Odd sum")