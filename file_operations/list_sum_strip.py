f = open('sample3','r')
list1 = []
for i in f:
    # list1.append(i) #['101\n', '102\n', '103\n', '104\n', '105\n', '106\n', '107\n', '108\n', '109\n', '110']
    # each enter key pressed in the file is read as \n
    # rstrip() function is used to strip a character in right side, for left use lstrip()
    j = i.rstrip('\n')
    k=int(j)
    list1.append(k)
print(list1)
print(sum(list1))