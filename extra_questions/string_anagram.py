a = 'listen'
b = 'silent'
c = 'list'

# method 1:
# if(sorted(a) == sorted(b)):
#     print("yes")
# else:
#     print("No")
# ------------------------------------------
# method 2:
dic1 = {}
dic2 = {}
for i in a:
    if i not in dic1:
        dic1[i] = 1
    else:
        dic1[i]+=1
for j in c:
    if j not in dic2:
        dic2[j] = 1
    else:
        dic2[j]+=1

if(dic2 == dic1):
    print('yes')
else:
    print("No")
for k,v in dic1.items():
    print(k,'-',v)
