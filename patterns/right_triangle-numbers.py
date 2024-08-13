# 0
# 0 1
# 0 1 2
# 0 1 2 3

rows = int(input("Enter the number of rows"))
for i in range(rows+1):
    for j in range(i):
        print(j, end=" ")
    print()

# ---------------------------------------------------------------------------

# 1
# 1 2
# 1 2 3
# 1 2 3 4

rows = int(input("Enter the number of rows"))
for i in range(rows+1):
    for j in range(i):
        print(j+1, end=" ")
    print()

# ------------------------------------------------------------------------------

# 1
# 2 3
# 4 5 6
# 7 8 9 10

rows = int(input("Enter the number of rows"))
num=1
for i in range(rows+1):
    for j in range(i):
        print(num, end=" ")
        num+=1
    print()