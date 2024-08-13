n = int(input("Enter the number to find the multiplication table"))
p = 1
for i in range(1,11):
    p = n*i
    print(n,"x",i,"=",p)