list1 = ['apple','cherry','banana']
vowels = 'aeiouAEIOU'
lst = [''.join(letter for letter in words if letter not in vowels)for words in list1]
print(lst)
