lst = [6,3,5,14,25,23,26,29,14,13,11,15,18,19]
prime_list=[]
for i in lst:
    for j in range(2,i):
        if(i%j == 0):
            break
    else:
        prime_list.append(i)
print(prime_list)
