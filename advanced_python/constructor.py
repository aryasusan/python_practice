# Constructor:
# - method used to instantiate an object,ie, to assign values to variables
# when an object of the class is created

class Student:
    college = 'Viswa'
    def __init__(self,id,fname,age,course):
        self.id =id
        self.fname = fname
        self.age = age
        self.course = course
    def print_value(self):
        print(self.id,self.fname,self.age,self.course,Student.college)

obj1 = Student(1,'arya',31,'python')
obj2 = Student(2,'babu',56,'python')

obj1.print_value()
obj2.print_value()
