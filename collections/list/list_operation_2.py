# element raised to power 1,2,3,4,5,6,7,8 correspondingly
lst =[1, 4, 7 ,8 ,2 ,3 ,5 ,9]
for i in lst:
    print (i**(lst.index(i)+1))

# print(7 in lst)  -- True
# print(12 not in lst) --- True
# print(4 not in lst) -- False