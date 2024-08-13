num = int(input("Enter the number"))
reversed_num = 0
while(num!=0):
    digit = num%10
    reversed_num = reversed_num*10 + digit
    num//=10
print(reversed_num)

# 153
#
# digit = 153%10 = 3
# reversed_num = 0*10 +3 = 3
# num = 153//10 = 15
#
# digit = 15%10 = 5
# reversed_num = 3*10 +5 =35
# num = 15//10 = 1
#
# digit = 1%10 = 1
# reversed_num = 35*10 +1 =351
# num = 1//10 = 0