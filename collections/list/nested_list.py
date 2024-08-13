# NESTED LIST

# can create multiple lists in a list,
# for eg, i can store details of each employee working in a company in a single list
list = [[1,'arya','susan',31],
        [2,'babu','jacob',66],
        [3,'beena','v',61]]
print(list)
for i in list:
    print(i[1::2])
list.extend([[1,2],[2,3]])
print(list)