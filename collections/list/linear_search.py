lst = [10,15,11,8,6,5,25,30,40,50,31,29]
number = int(input("enter the number"))
found = False
for i in lst:
    if(i==number):
        found = True
        break
    else:
        found = False
if(found):
    print("Element found")
else:
    print("Element not found")

# linear search algorithm
#  --More time complexity