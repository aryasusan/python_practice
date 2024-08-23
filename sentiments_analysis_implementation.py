str1 = input("enter the comment")
words = str1.split()
pos_dic = {'1':'good','2':'excellent'}
neg_dic = {'1':'bad','2':'worst'}
count = 0
for i in words:
    if i in pos_dic.values():
        count+=1
    elif i in neg_dic.values():
        count-=1
    else:
        count+=0
print(count,'count value')
if count>0:
    print("positive comment")
elif count<0:
    print("negative comment")
else:
    print("neutral comment")

