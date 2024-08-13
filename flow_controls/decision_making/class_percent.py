no_of_classes = int(input("Enter number of classes: "))
no_of_class_attended = int(input("Enter number of classes attended: "))
percent = (no_of_class_attended/no_of_classes) * 100
print("percent classes", percent)
if(percent>=75):
    print("You can write exam")
else:
    print("you cannot write exam")