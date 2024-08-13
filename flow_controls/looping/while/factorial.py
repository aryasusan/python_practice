n = int(input("Enter the number to find the factorial"))
i = 1
f = 1
while(i<=n):
    f *=i
    i += 1
print(f)

# method 2:
n = int(input("Enter the number to find the factorial"))
f = 1
while(n>=1):
    f *=n
    n -=1
print(f)