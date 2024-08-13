for i in 'arya':
    print(i)

# prints each character

# ------------------------------------------

data = "luminar technolab"
for i  in data:
    if(i=="a"):
        break
    print(i)

# prints  l u m i n   in each line

data = "luminar technolab"
for i  in data:
    if(i=="a"):
        continue
    print(i)

# prints  l u m i n r  t e c h n o l b     in each line, reads space as well

# data = "luminartechnolab"
for i  in data:
    if(i=="a"):
        pass
    print(i)

# prints  l u m i n a r t e c h n o l a b     in each line

# ---------------------------------------------------------------------


for i in range(-2,-5,-1):
    print(i)

# prints -2,-3,-4

# ------------------------------------------------------

a,b =10,5
if(a+b):
    print("hello")
else:
    print("world")

# prints hello, 15 is non-zero(true) so enters the if loop

a,b =5,5
if(a-b):
    print("hello")
else:
    print("world")

# prints world, value is 0(false),enters the else loop

# ---------------------------------------------------------------------

x=0
for i in range(10): #(0,..9) i=0,....i=9
    for j in range(-1,-10,-1):#(-1,..-9) j=-1 - x=1,j=-2 - x=2....x=9, j=-1 - x=10,j=-2 - x=11....x=19..repeats 9 times..x=90
        x+=1
print(x)

# x will be 90