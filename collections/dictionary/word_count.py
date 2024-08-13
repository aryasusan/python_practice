# count the number of occurrence of each word in a sentence/paragraph
    # split word by word into data -- line.split(' ') --separates by space and inserts to list
    # create an empty dict, and if word not present insert that word as key and value as 1, if present increment the value by 1

line = 'cat rat cat bat mango cat rat mango rat bat cat mango mango bat'
data = line.split(' ')
print(data)

dict1 = {}
for i in data:
    if i not in dict1:
        dict1[i] = 1
    else:
        dict1[i]+=1

# value = 1
# for i in data:
#     if i not in dict1:
#         dict1[i] = value
#     else:
#         dict1[i] = value + 1

print(dict1)
for j in dict1:
    print(j,dict1[j])

for k,v in dict1.items():
    print(k,':',v)