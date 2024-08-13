# rows = int(input("Enter the number of rows"))
# for i in range(rows):
#     for j in range(rows):
#         print("* ",end=" ")
#     print()

#
# ---------------------------------------------------------------------------------

# hollow square
# * * * *
# *     *
# *     *
# * * * *
rows = int(input("Enter the number of rows"))
for i in range(rows):
    for j in range(rows):
        if(i==0)|(i==rows-1)|(j==0)|(j==rows-1):
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()