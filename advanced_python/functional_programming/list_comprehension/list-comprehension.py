# 3 methods:

# 1. range of elements added into a list
# 2. range of elements added into a list using single condition
# 3. range of elements added into a list using multiple conditions

# 1. variable_name = [output range]
numbers = [i for i in range(1,11)]
print(numbers)

# square 1-20
squares = [i**2 for i in range(1,21)]
print(squares)

cube = [(i,i**3) for i in range(1,51)]
print(cube)

# 2. variable_name = [output range condition]
even = [i for i in range(1,26) if(i%2==0)]
print(even)

divisble_5 = [i for i in range(1,51) if(i%5==0)]
print(divisble_5)

# 3. variable_name = [output1 if_condition1 else output2 range]
# No elif condition,give as much if-else
#  variable_name = [output1 if_condition1 else output2 if_condition2 else output3 range]
lst = [(i,i**2) if(i%2==0) else (i,i**3) for i in range(1,21)]
print(lst)