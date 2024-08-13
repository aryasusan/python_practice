# divisible by 8
lst = [i for i in range(1,1001) if(i%8==0)]
print(lst)

#numbers having 6
lst1 = [i for i in range(1,1001) if('6' in str(i))]
print(lst1)

string = 'Practise list comprehension problems to drill your head'

# count number of vowels in a string
vowels = 'aeiouAEIOU'
lst3 = [i for i in string if(i in vowels)]
print(len(lst3))

# count number of spaces
lst3 = [i for i in string if(i==' ')]
print(len(lst3))

# find the word in a string that are less than 5 letters
lst4 = [i for i in string.split() if len(i)<5]
print(lst4)

