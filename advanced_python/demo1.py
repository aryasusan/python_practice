class Person:
    def set_value(self,fname,lname,age,loc):
        self.first = fname
        self.last = lname
        self.age = age
        self.loc = loc
    def print_value(self):
        print(self.first,self.last,self.age)

object1 = Person()
object1.set_value('arya',"susan",31,"mvpa")
object1.print_value()