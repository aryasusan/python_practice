# take 3 inputs from the user and a number n,
# such that sum of 3 should not be equal to n,
# find all such possible combinations as[i,j,k]
# where values of i,j,k ranges from 0to x,y,z correspondingly
x=int(input('Enter number 1'))
y=int(input('Enter number 2'))
z=int(input('Enter number 3'))
n=int(input('Enter the sum'))
list = []
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if(i+j+k != n):
                list.append([i,j,k])
print(list)

# for better reading
for each in list:
    print(each)

#list comprehension
new_list=[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if(i+j+k !=n)]
print(new_list,'comprehended')
