list = [1,5,3,7,10,15,30]
print(list[-0]+list[1]+list[-2]) #answer will be 21 (1+5+15)
# list[-0]-- reads as list[0]

#----------------------------------------------------------------------

lst = [4,10,6,20,15,5,30,7,3]
# create a new list [96,90,94,80,85,95,70,93,97]

sum=sum(lst)
new_list = []
for i in lst:
    new_element = sum-i
    new_list.append(new_element)
print(new_list)

#-------------------------------------------------------------------------

lst2 = [1,2,4,3,2,1,3,5,6,7,8,6,5,3,2,6,9,10,11,9,7,6,4,5,6]

# new list = [1,4,1,8,2,11,4] --pick elements whenever series increase or decrese
new_list1 = []
for i in lst2:
    if(lst2.index(i)>0):
        left_index = lst2.index(i)-1
        right_index = lst2.index(i)+1
        if((lst2[left_index]>i<lst2[right_index])|(lst2[left_index]<i>lst2[right_index])):
            new_list1.append(i)
    else:
        new_list1.append(i)
print(new_list1)

#------------------------------------------------------------------------------------

list3 = [3,6,1,4,2,8,10,15,5]

# print the sum pairs of given number, if user enters 6, the pairs are(3,3)(1,5)(5,1)(2,4)(4,2)

number = int(input("Enter a number"))
for i in list3:
    for j in list3:
        if(i+j == number):
            print(i,j)