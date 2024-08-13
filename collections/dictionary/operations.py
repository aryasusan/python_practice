dict1 = {'id':10,'fname':'arya','lname':'babu','age':31,'proff':'student'}
print(dict1)

# to collect value from a dictionary, use the particular key
print(dict1['fname'])

# to update,use the key
dict1['age'] = 38
print(dict1)

dict1['age']+=7
print(dict1)

#insert a new key:value
dict1['marks']=[40]
print(dict1)

dict1['marks'].append(41)
dict1['loc'] = []
dict1['loc'].append('ajsk')
for i in dict1: #i will be key
    print(i,dict1[i])

print('fname' in dict1) #--True
print('fname' not in dict1) #--False
