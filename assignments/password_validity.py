import re
passwrd = input("enter password:")
valid = True
while True:
    if(len(passwrd)<=8):
        valid = False
        break
    elif not re.search("[a-z]",passwrd):
        valid = False
        break
    elif not re.search("[A-Z]",passwrd):
        valid = False
        break
    elif not re.search("[0-9]",passwrd):
        valid = False
        break
    elif not re.search("[_@$]",passwrd):
        valid = False
        break
    else:
        valid = True
        print("password is valid")
        break
if(valid==False):
    print("Invalid passwrd")