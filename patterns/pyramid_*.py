
#       *
#     * * *
#   * * * * *
# * * * * * * *

# for i in range(4):
#     for j in range(7):
#         if((j<3-i) | (j>3+i)):
#             print(" ",end=" ")
#         else:
#             print("*", end=" ")
#     print()
# --------------------------------------------------------------------------------

#       *
#     *   *
#   *   *   *
# *   *   *   *

# rows = int(input("enter the number of rows"))
# for i in range(rows):
#     for j in range(rows+3):
#         if(((i==0)&(j==3))|
#                 ((i==1)&((j==2)|(j==4)))|
#                 ((i==2)&((j==1)|(j==3)|(j==5)))|
#                 ((i == 3) & ((j == 0) | (j == 2) | (j == 4)| (j == 6)))):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#
#     print()
# --------------------------------------------------------------------------

    # *   *   *   *
    #   *   *   *
    #      *  *
    #        *

# rows = int(input("enter the number of rows"))
# for i in range(rows):
#     for j in range(rows+3):
#         if(((i==3)&(j==3))|
#                 ((i==2)&((j==2)|(j==4)))|
#                 ((i==1)&((j==1)|(j==3)|(j==5)))|
#                 ((i == 0) & ((j == 0) | (j == 2) | (j == 4)| (j == 6)))):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#
#     print()

# ----------------------------------------------------------------------------------

rows = int(input("enter the number of rows"))
for i in range(rows):
    for j in range(rows+(rows-2)+1):
        if(((i==1)&((j==0)|(j==6)))|
           ((i==2)&((j==0)|(j==1)|(j==5)|(j==6)))|
           ((i==3)&((j==0)|(j==1)|(j==2)|(j==4)|(j==5)|(j==6)))):
            print(" ",end=" ")
        else:
            print("*", end=" ")
    print()
