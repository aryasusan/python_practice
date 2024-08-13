string = 'luminartechnolab'
vowels = 'aeiouAEIOU'
vowels_list = [i for i in string if i in vowels]
print(len(vowels_list))

consonants_count = len([i for i in string if i not in vowels])
print(consonants_count)