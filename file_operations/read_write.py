f = open('sample5', 'r')
w = open('sample5_copy','w')
for i in f:
    w.write(i)
