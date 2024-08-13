upper_limit = int(input("Enter the upper limit"))
lower_limit = int(input("Enter the lower limit"))
sum_even = 0
sum_odd = 0
for i in range(lower_limit, upper_limit+1):
    if(i%2 == 0):
        sum_even+=i
    else:
        sum_odd +=i
print(sum_even,"Even sum")
print(sum_odd,"Odd sum")