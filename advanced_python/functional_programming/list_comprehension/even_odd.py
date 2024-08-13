lst = [(i,'even') if(i%2 == 0) else(i,'odd') for i in range(1,31)]
print(lst)

lst2 = [(i,'small') if(1<=i<=15) else(i,'median') if(16<=i<=35) else(i,'large') for i in range(1,51)]
print(lst2)