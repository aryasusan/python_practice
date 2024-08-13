set1 = {1,2,3,4,5}
set1.remove(3)
print(set1)
set1.pop()
print(set1) #pop removes single element randomly
set1.difference_update([1,5]) #remove multiple elements ie 1 and 5
print(set1)
set1.discard(2) # removes element 2 if present
# remove function will throw error if the element is not present,
# but discard function will not throw error