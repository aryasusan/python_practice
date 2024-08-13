list = [1,2,3,4,5,6,78,2,3,8,9]
print(list[2:5]) # prints elements from index 2 to index 4
print(list[2:]) # prints from index 2 to end
print(list[:4]) #prints from index 0 to 3
print(list[1:7:2]) # prints elements in index1,3,5 -start:stop:step
print(list[1::3]) #prints elements in index1,4,7,10 start::step
print(list[::5]) #prints elements in 0,5,10 ::step, from start to end with step count

# negative indexing starts from -1 to -n
print(list[-1]) #last index ie 9