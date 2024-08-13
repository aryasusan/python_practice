print("1- Create a new file\n2-Display the file\n3-Add a new item")
selection = int(input("enter the selection"))

if(selection==1):
    subject = input("enter the subject")
    f = open('Subject.txt','w')
    f.write(subject+'\n')
elif(selection==2):
    try:
     f = open('Subject.txt','r')
     contents = f.read()
     print(contents)
    # for i in f:
    #     print(i)
    except:
        print('file not found')
elif(selection==3):
    subject = input("enter the subject")
    f = open('Subject.txt','a')
    f.write(subject+'\n')
    read = open('Subject.txt','r')
    for i in read:
        print(i)
else:
    print("Invalid selection")