inp = "d2f10g2"
output = "ddffffffffffgg"

a = ''
b = ''
for i in inp:
    if i.isdigit():
        a+=i
    else:
        a+=" "
        b+=i+" "
a = a.split()
b = b.split()
for i in range(len(b)):
    print(b[i]*int(a[i]), end='')