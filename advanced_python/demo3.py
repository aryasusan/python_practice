class Student:
    def set_value(self,id,fname,age,course,college):
        self.id =id
        self.fname = fname
        self.age = age
        self.course = course
        self.college = college
    def print_value(self):
        print(self.id,self.fname,self.age,self.course,self.college)

obj1 = Student()
obj1.set_value(1,'arya',31,'python','viswa')
obj2 = Student()
obj2.set_value(2,'babu',56,'python','sn')

obj3 = Student()
obj3.set_value(3,'beena',43,'ml','mits')

obj4 = Student()
obj4.set_value(4,'basil',30,'ds','ma')

obj5 = Student()
obj5.set_value(5,'jacob',35,'ba','ilahia')

obj1.print_value()
obj2.print_value()
obj3.print_value()
obj4.print_value()
obj5.print_value()