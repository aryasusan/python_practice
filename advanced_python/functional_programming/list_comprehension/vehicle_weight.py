dic = {'bike': 350,'cycle':50,'car':2000,'jeep':3000,'bus':5000,'suv':3500}
lst = [k.swapcase() for k,v in dic.items() if(v>2500)]
print(lst)