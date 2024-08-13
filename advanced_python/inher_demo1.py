class Personal_data():
    def get_pers_data(self,id,fname,lname,age):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.age = age
    def print_pers_data(self):
        print(self.id,self.fname,self.lname,self.age, end=' ')

class Proff_data(Personal_data):
    def get_prof_data(self,prof,salary,location):
        self.prof = prof
        self.salary = salary
        self.location = location

    def print_data(self):
        print(self.prof,self.salary,self.location)

obj1 = Proff_data()
obj1.get_prof_data('Python',3000,'Kochi')
obj1.get_pers_data(1,'arya','susan',31)
obj1.print_pers_data()
obj1.print_data()

