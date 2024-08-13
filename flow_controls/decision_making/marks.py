sub1= int(input("enter marks of subject 1: "))
sub2= int(input("enter marks of subject 2: "))
sub3= int(input("enter marks of subject 3: "))
sub4= int(input("enter marks of subject 4: "))

total = sub1 + sub2 + sub3 +sub4

if(total>=180):
    print("A+")
elif(160<=total<=179):
    print("A")
elif(total<=159) & (total>=140):
    print("B+")
elif(total<=139) & (total>=120):
    print("B")
elif(total<=119) & (total>= 100):
    print("C+")
else:
    print("FAIL")