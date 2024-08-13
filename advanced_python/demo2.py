class Employee:
    def set_value(self,id,fname,lname,age,proff,salary):
        self.id =id
        self.fname = fname
        self.lname = lname
        self.age = age
        self.proff = proff
        self.salary = salary
    def print_value(self):
        print(self.id,self.fname,self.lname,self.age,self.proff,self.salary)

obj1 = Employee()
obj1.set_value(1,'arya','susan',31,'student','1000')
print(obj1.id)

obj2 = Employee()
obj2.set_value(2,'babu','jacob',56,'python','2000')

obj3 = Employee()
obj3.set_value(3,'beena','babu',43,'ml','3000')

obj4 = Employee()
obj4.set_value(4,'basil','peter',30,'ds','5000')

obj5 = Employee()
obj5.set_value(5,'jacob','babu',35,'ba','8000')

obj1.print_value()
obj2.print_value()
obj3.print_value()
obj4.print_value()
obj5.print_value()