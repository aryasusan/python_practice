class Employee:
    department = 'Operations'
    company_name= 'UST'
    def set_value(self,id,fname,lname,age):
        self.id =id
        self.fname = fname
        self.lname = lname
        self.age = age
    def print_value(self):
        print(self.id,self.fname,self.lname,self.age,Employee.department,Employee.company_name)

obj1 = Employee()
obj1.set_value(1,'arya','susan',31)

obj2 = Employee()
obj2.set_value(2,'babu','jacob',56)

obj3 = Employee()
obj3.set_value(3,'beena','babu',43)

obj4 = Employee()
obj4.set_value(4,'basil','peter',30)

obj5 = Employee()
obj5.set_value(5,'jacob','babu',35)

obj1.print_value()
obj2.print_value()
obj3.print_value()
obj4.print_value()
obj5.print_value()