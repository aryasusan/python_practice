# * * * *
# * * *
# * *
# *

# method1
# rows = int(input("Enter the number of rows"))
# for i in range(rows,0,-1):
#     for j in range(i):
#         print("*", end=" ")
#     print()

# method 2:
# rows = int(input("Enter the number of rows"))
# for i in range(rows):
#     for j in range(rows-i):
#         print("*", end=" ")
#     # for j in range(i):
#     #     print(" ", end=" ")
#     print()

# ------------------------------------------------------------------------

# * * * *
#   * * *
#     * *
#       *

rows = int(input("Enter the number of rows"))
for i in range(rows):
    for j in range(i):
        print(" ",end=" ")
    for j in range(rows-i):
        print("*", end=" ")
    print()

