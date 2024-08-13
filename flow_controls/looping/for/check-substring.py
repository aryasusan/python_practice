string = input("enter string")
sub_string= input("enter sub string")
count=0
for i in range(len(string)):
    if(string[i:len(string)].startswith(sub_string)):
        count+=1
print(count)