list = [10,10,20,30,'big data','big data','python']
new_list = []
for i in list:
    if i not in new_list:
        new_list.append(i)
print(new_list)