# if unit<100 free
#     unit is between 101-200 per unit charge is 5
#     unit is above 200 per unit charge is 10
# if unit is 350, bill will be 100*5 + 150*10 = 2000
# (1st 100 units is free, next 100 units is per 5 and final 150 units is per 10)

unit = int(input("enter units: "))
if(unit>200):
    bill = (100*5) +((unit-200)*10)
elif(101<=unit<=200):
    bill = (unit-100)*5
else:
    bill = 0
print(bill,"bill")