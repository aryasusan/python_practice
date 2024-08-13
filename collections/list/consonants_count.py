string = 'luminartechnolab'
vowels = 'aeiouAEIOU'
list = []
for i in string:
    if i not in vowels:
        list.append(i)
print(len(list))