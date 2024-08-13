list=['apple','orange','dfg','grape','qwr','mango','jkl','omn','mnp']
vowels='aeiouAEIOU'
new_list=[]
for i in list:
    for j in i:
        if j in vowels:
            new_list.append(i)
            break
print(new_list)