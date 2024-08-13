# *
# * *
# * * *
# * * * *

# rows = int(input("Enter the number of rows"))
# for i in range(rows):
#     for j in range(i+1):
#         print("*", end=" ")
#     print()

# -------------------------------------------------------------------------

#   j=1 2 3 4
#i=1        *
#  2      * *
#  3    * * *
#  4  * * * *

# rows = int(input("Enter the number of rows"))
# for i in range(1,rows+1):
#     for j in range(1,rows+1):
#         if(j<= rows-i):
#             print(" ",end=" ")
#         else:
#             print("*",end=" ")
#     print()

# __________________________________________________________________________________

#       *
#     * *
#   * * *
# * * * *

# for i in range(4):
#     for j in range(4):
#         if(j<3-i):
#             print(" ",end=" ")
#         else:
#             print("*", end=" ")
#     print()

# rows = int(input("enter the number of rows"))
# for i in range(rows):
#     for j in range(rows):
#         if(j<(rows-1)-i):
#             print(" ", end=" ")
#         else:
#             print("*", end=" ")
#     print()