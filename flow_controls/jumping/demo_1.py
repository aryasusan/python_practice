# jumping statements:
    # break,continue,pass

# break:
#     stops the loop at a stage and exit

# for i in range(1,51):
#     if(i==25):
#         break
#     print(i)

# prints from 1 to 24-- when i ==25, enters the if loop,break and exit from for loop,
#  doesnot print i=25 as print statement is inside for loop

# ------------------------------------------------------------------------------------------------
# continue:
#     skips the condition(the statements written inside the loop will not be executed) and
#     then continues the loop

# for i in range(1,51):
#     if(i==25):
#         continue
#     print(i)
# prints from 1 to 50 but 25 will not be printed
# ------------------------------------------------------------------------------------------------------------

# pass:
#     do nothing

for i in range(1,51):
    if(i==25):
        pass
    print(i)

num = int(input("enter the number"))
if(num%2 == 0):
    print("Number is even")
else:
    pass
# prints from 1 to 50 just like normal