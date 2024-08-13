f = open('temperature','r')
details={}
new_details={}
for i in f:
    data = i.rstrip('\n').split(',')
    district=data[0]
    temp=data[1]
    if district not in details:
        details[district]=temp
    else:
        old_temp=details[district]
        if(temp>old_temp):
            new_details[district]=temp
for k,v in new_details.items():
    print(k,'-',v)

# /method2
#     if district not in details:
#         details[district]=temp
#     else:
#         details[district].append(temp)
# for k, v in details.items():
#     if (v[0] > v[1]):
#         print(k, '-', v[0])
#     else:
#         print(k, '-', v[1])