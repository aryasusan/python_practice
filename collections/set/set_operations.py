# 1. Union
# 2. Intersection
# 3. Difference

set1 = {1,2,3,4,5,6,7,8,9}
set2 = {5,6,10,11,3,2}
set3 = {10,15,20,3,4,100}
print(set1.intersection(set2).intersection(set3))
print(set1.union(set2).union(set3))
print(set1.difference(set2)) # element present in set1 but not in set2