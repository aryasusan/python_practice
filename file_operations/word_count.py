line=open('sample4','r')
dict1 = {}
for i in line:
    word = i.rstrip('\n').split(' ')
    for j in word:
        if j not in dict1:
            dict1[j] = 1
        else:
            dict1[j]+=1
print(dict1)
print(dict1.items())
for k,v in dict1.items():
    print(k,':',v)