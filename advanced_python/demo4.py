class Student:
    college = 'Viswa'
    def set_value(self,id,fname,age,course):
        self.id =id
        self.fname = fname
        self.age = age
        self.course = course
    def print_value(self):
        print(self.id,self.fname,self.age,self.course,Student.college)

obj1 = Student()
obj1.set_value(1,'arya',31,'python')
obj2 = Student()
obj2.set_value(2,'babu',56,'python')

obj3 = Student()
obj3.set_value(3,'beena',43,'ml')

obj4 = Student()
obj4.set_value(4,'basil',30,'ds')

obj5 = Student()
obj5.set_value(5,'jacob',35,'ba')

obj1.print_value()
obj2.print_value()
obj3.print_value()
obj4.print_value()
obj5.print_value()