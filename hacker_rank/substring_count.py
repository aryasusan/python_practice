string1 = input("enter the string")
substring = input("enter the substring")
count = 0

for i in range(len(string1)):
    print(string1[i:len(string1)])
    if(string1[i:len(string1)].startswith(substring)):
        count+=1
        print(count)
print(count)