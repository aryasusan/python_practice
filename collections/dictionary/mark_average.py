# hackerarank question-- find the average of marks obatined by the student
# upto 2 decimal places
name = input("enter students name")
student_marks = {}
student_marks['arya']=[2,3,4]
student_marks['susan']=[3,4]
student_marks['babu']=[7,8,9,9]
print(format(sum(student_marks[name])/len(student_marks[name]),'.2f'))
