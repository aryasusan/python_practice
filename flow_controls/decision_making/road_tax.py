price = int(input("Enter price of the bike"))
if(price>100000):
    tax=(15/100)*price
elif(50000<=price<=100000):
    tax=(10/100)*price
else:
    tax=(5/100)*price
print(tax,"tax amount")