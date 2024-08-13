list = [[1,'arya','susan',31,'big data',5000],
        [2,'babu','jacob',24,'python',1000],
        [3,'beena','v',61,'testing',1250],
        [4,'jacob','babu',25,'big data',3000]]

sum = 0
for i in list:
    if(i[3]>26):
        print(i[1:5],"age above 26")
    if (i[3]==25):
        print(i[1:5],"age is 25")
    if(i[4]=='big data'):
        print(i[1::2],"prof is big data")
    if((i[3]>26) & (i[5]>1250)):
        print(i[1:3],"age above 26 and salary above 1250")
    if((i[4] == 'big data')&(i[3]>26)):
        print(i[1:4],"prof is big data and age above 27")
    sum+=i[5]
print(sum,'total salary')