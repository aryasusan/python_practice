# for i in range(4):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
# --------------------------------------------------------------

#       *
#     * *
#   * * *
# * * * *
#
# for i in range(4):
#     for j in range(4):
#         if(j<3-i):
#             print(" ",end=" ")
#         else:
#             print("*", end=" ")
#     print()
# ---------------------------------------------------------------------


# * * * *
# * * *
# * *
# *

# for i in range(4):
#     for j in range(4-i):
#         print("*", end=" ")
#     print()

# -------------------------------------------------------------------------

# * * * *
#   * * *
#     * *
#       *
#
# for i in range(4):
#     for j in range(i):
#         print(" ", end=" ")
#     for j in range(4-i):
#         print("*", end=" ")
#     print()

# ------------------------------------------------------------------

# *
# * *
# *   *
# *     *
# * * * * *

# for i in range(5):
#     for j in range(i+1):
#         if((i==2) & (j==1)) |((i==3)&((j==1)|(j==2))): # brackets are important
#             print(" ", end=" ")
#         else:
#             print("*", end=" ")
#     print()

# rows = int(input("enter the number of rows"))
# for i in range(rows):
#     for j in range(i+1):
#         if((2<=i<rows-1) & (0<j<i)):
#             print(" ", end=" ")
#         else:
#             print("*", end=" ")
#     print()

# --------------------------------------------------------------------------------------

#       *
#     *   *
#   *   *   *
# *   *   *   *

# for i in range(4):
#     for j in range(7):
#         if(((i==0)&(j==3))|
#           ((i==1)&((j==2)|(j==4)))|
#           ((i==2) &((j==1)|(j==3)|(j==5)))|
#           ((i==3) &((j==0)|(j==2)|(j==4)|(j==6)))):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# ---------------------------------------------------------------------------------------


#       *
#     * * *
#   * * * * *
# * * * * * * *

for i in range(4):
    for j in range(7):
        if((j<3-i) | (j>3+i)):
            print(" ",end=" ")
        else:
            print("*", end=" ")
    print()




