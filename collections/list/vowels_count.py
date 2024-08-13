string = 'luminartechnolab'
vowels = 'aeiouAEIOU'

# method 1:

count = 0
for i in string:
    for j in vowels:
        if(j==i):
            count+=1
print(count)

# method 2:

list=[]
for k in string:
    if k in vowels:
        list.append(k)
print(len(list))