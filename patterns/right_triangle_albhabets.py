# ASCII of A = 65
# ASCII of Z = 90
# ASCII of a = 97
# ASCII of z = 122

# A
# A B
# A B C
# A B C D

# ASCII of A = 65
# char_num = 65
# rows = int(input("Enter the number of rows"))
# for i in range(rows+1):
#     for j in range(i):
#         print(chr(char_num), end=" ")
#         char_num+=1
#     char_num = 65
#     print()

# --------------------------------------------------------------------------------

# A
# B C
# D E F
# G H I J

# ASCII of A = 65
char_num = 65
rows = int(input("Enter the number of rows"))
for i in range(rows+1):
    for j in range(i):
        print(chr(char_num), end=" ")
        char_num+=1
    print()