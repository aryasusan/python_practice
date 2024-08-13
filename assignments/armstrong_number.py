#armstrong number = sum of powers of each digit is equal to the number itself, power will be the length of the number
# eg 153 = 1^3 + 5^3 + 3^3 (1+125+27)
num = int(input("enter the number to check if its an armstrong number:"))
length_num = len(str(num))
sum = 0
temp = num
while temp>0:
    digit = temp%10
    sum+=digit**length_num
    temp//=10
if(sum==num):
    print('Yes')
else:
    print('No')

