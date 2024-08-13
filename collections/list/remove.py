list = [1,2,3,4,5,6,78,2,3,8]
list.remove(2) #removes first occurance only
print(list)
list.pop() # deletes last element
print(list)
list.pop(3) # removes element in index 3
del list[1:3]
print(list)

# in remove we pass the element to be deleted
# but in pop, we pass the index of the element to be deleted