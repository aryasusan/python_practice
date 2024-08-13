# 1
# 2 2
# 3 3 3
# 4 4 4 4

# rows = int(input("Enter the number of rows"))
# for i in range(rows):
#     for j in range(i+1):
#         print(i+1, end=" ")
#     print()
# ----------------------------------------------------------------------------------

# 1
# 2 1
# 3 2 1
# 4 3 2 1
# rows = int(input("Enter the number of rows"))
# for i in range(rows):
#     for j in range(i+1,0,-1):
#         print(j, end=" ")
#     print()

# -------------------------------------------------------------------------------

# 4 4 4 4
# 3 3 3
# 2 2
# 1

# method 1
# rows = int(input("Enter the number of rows"))
# for i in range(rows+1):
#     for j in range(i+1,rows+1):
#         print(rows-i, end=" ")
#     print()

# method2
# rows = int(input("Enter the number of rows"))
# for i in range(rows,0,-1):
#     for j in range(i):
#         print(i, end=" ")
#     print()

# --------------------------------------------------------------------------------------

# 1 1 1 1
# 2 2 2
# 3 3
# 4

# method 1
# rows = int(input("Enter the number of rows"))
# for i in range(rows+1):
#     for j in range(i+1,rows+1):
#         print(i+1, end=" ")
#     print()

# method 2
# rows = int(input("Enter the number of rows"))
# for i in range(rows,0,-1):
#     for j in range(i):
#         print(rows-i+1, end=" ")
#     print()

# -------------------------------------------------------------------------


# 0 1 2 3
# 0 1 2
# 0 1
# rows = int(input("Enter the number of rows"))
# for i in range(rows-1,0,-1):
#     for j in range(i+1):
#         print(j, end=" ")
#     print()

# ---------------------------------------------------------------------------------

# 0
# 0 1
# 0 2 4
# 0 3 6 9
# 0 4 8 12 16
# 0 5 10 15 20 25

# row 0-1colum,row1-2 columns,row2-3 columns....so j from 0 to i+1,values are multiples
for i in range(0,6):
    for j in range(0,i+1):
        print(i*j,end=" ")
    print()

