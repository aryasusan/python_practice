# &,| --pipe,^ --cap  ==> AND, OR, XOR

#AND &
# 0 0 0
# 0 1 0
# 1 0 0
# 1 1 1

#OR  |
# 0 0 0
# 0 1 1
# 1 0 1
# 1 1 1

#XOR ^
# 0 0 0
# 0 1 1
# 1 0 1
# 1 1 0

num1 = 4  #binary num is 0100
num2 = 6 # 0110
print(num1 & num2) # 4  0100
                   # 6  0110
                   # &  0100  =4
num1 = 2
num2 = 4
print(num1 & num2) # 0
