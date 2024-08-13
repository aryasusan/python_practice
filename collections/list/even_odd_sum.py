list=[]
for i in range(1,51):
    list.append(i)
print(list)

even_list = []
for i in list:
    if(i%2 == 0):
        even_list.append(i)
print(even_list)

odd_list=[]
for j in list:
    if(j%2 == 1):
        odd_list.append(j)
print(odd_list)

print(sum(list),"total")
print(sum(even_list),"even total")
print(sum(odd_list),"odd total")