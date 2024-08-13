lst = [i for i in range(1,21) if(i%3==0 or i%5==0)]
print(lst)

for i in range(1,11):
    if(i%4==0):
        break
    print(i)

str = input("enter string to reverse")
name = str[::-1] or 'N/A'
print(name)