f = open('Temperatureyear', 'r')
details={}
new_details={}
for i in f:
    data = i.rstrip('\n').split()
    year=data[0]
    temp=int(data[1])
    if year not in details:
        details[year]=temp
    else:
        old_temp=details[year]
        if(temp>old_temp):
            new_details[year]=temp
for k,v in new_details.items():
    print(k,'-',v)

# /method2
#     if year not in details:
#         details[year]=[temp]
#     else:
#         details[year].append(temp)
# for k, v in details.items():
#     v.sort(reverse=True)
#     print(k, '-', v[0])