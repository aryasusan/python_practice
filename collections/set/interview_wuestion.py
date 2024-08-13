# remove duplicate element from a list and print the sorted the list in ascending order
list1 = [1,2,3,4,5,1,3,4,10,11]
set1 = set(list1)
print(set1)
list1=list(set1)
list1.sort()
print(list1)