# set is defined using {}, but set={} will be dictionary so,
# an empty set can be created only using set()
empty_set = {}
print(type(empty_set))
empty_set=set()
empty_set = {1,2,3,4,'big data',5,6,1,2,3,4,True,False} #true will not be printed as value is 1 which is duplicate
print(empty_set)
print(type(empty_set))

# supports heterogenous data
# insertion order is not preserved, the elements are inserted randomly
# does not support duplicate values
# set is mutable
