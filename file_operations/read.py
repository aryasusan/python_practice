# location of sample1 and this file is in same package so only file name
# needs to be passed
# else full path shud be given

f = open('sample1','r')
for i in f:
    print(i)

# rightclick and take absolute path
f1= open('/home/arya/PycharmProjects/core_python/sample2','r')
for j in f1:
    print(j)

# if in external location: right click-properties- take parent folder
f2=open('/home/arya/Documents/sample5','r')
for k in f2:
    data = k.rstrip('\n').split(',')
    print(data)