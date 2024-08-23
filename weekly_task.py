# *
# * *
# * * *
# * * * *
# * * * * *

for i in range(1,6):
    for j in range(i):
        print("*",end=" ")
    print()


 # -----------------------------------------------------------
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
for i in range(1,6):
    for j in range(i):
        print(i, end=" ")
    print()

# --------------------------------------------------------

# * * * * *
# * * * *
# * * *
# * *
# *
for i in range(1,6):
    for j in range(i,6):
        print("*", end=" ")
    print()

# ---------------------------------------------------------

# * * * *
# * * *
# * *
# *
# * *
# * * *
# * * * *
for i in range(1,5):
    for j in range(i,5):
        print("*", end=" ")
    print()
for i in range(5,8):
    for j in range(i-3):
        print("*",end=" ")
    print()
# ---------------------------------------------------------------

#         1
#       1 2 1
#     1 2 3 2 1
#   1 2 3 4 3 2 1

for i in range(1,5):
    for j in range(5-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    for j in range(i-1,0,-1):
        print(j,end=" ")
    print()
