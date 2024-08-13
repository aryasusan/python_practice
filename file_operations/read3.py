# age above 50--fname,lname,age,proffesion
# age range 25 to 40--fname,lname,age,prof
# india work--fname,lname,age,prof
# us work--fname,lname,age,prof
# each location count

f = open('/home/arya/Downloads/customer1.txt','r')
dict1={}
for i in f:
    data = i.rstrip('\n').split(',')
    age = data[3]
    location = data[-1]
    if(age>'55'):
        print(data[1:-1])
    if ('25'<age<'40'):
        print(data[1:-1])
    if(location=='India'):
        print(data[1:-1])
    if(location not in dict1):
        dict1[location]=1
    else:
        dict1[location]+=1
print(dict1)
for k,v in dict1.items():
    print(k,'-',v)