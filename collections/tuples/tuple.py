# tuple is defined using paranthesis ()
#     tup = () #empty
#     tup = tuple() #using function
# supports heterogeneous data
#     tup = (1,2,'a','b',1.1)
# insertion order is preserved
# supports duplicate values
# tuple is immutable ie, values cannot be altered as tuple do not have index

tup = (1,2,3,4,5,25,50,45)
list1 =list(tup)
list1[5]=500
tup = tuple(list1)
print(tup)