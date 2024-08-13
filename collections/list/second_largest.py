list = [2,1,3,2,4,5,6,7,9,7,6,8,10,12,15,15]
# list.sort() # ascending sort
list.sort(reverse=True) #descending order
print(list)
unique_list =[]
for i in list:
    if i not in unique_list:
        unique_list.append(i)
print(unique_list[1])