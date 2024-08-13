# map - for transforming each element in a collection
# filter - to collect some elements by using some conditions
# output of both will be in a list
#
# variable_name = list(map(function,iterable))
# variable_name = list(filter(function,iterable))

list1 =[1,2,3,4,5]
square_list =list(map(lambda i:i**2,list1))
print(square_list)

even_list =list(filter(lambda i:i%2==0,list1))
print(even_list)

#cube of odd numbers from the list
list2 = [1,2,3,4,5,6,7,8,9,10]
odd_list = list(filter(lambda i:i%2==1,list2))
cube_list = list(map(lambda i:i**3,odd_list))
print(cube_list)