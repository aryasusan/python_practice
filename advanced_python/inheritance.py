class A(): #Parent class
    def method_a(self,num1):
        self.num1 = num1
        print('Inside class A', self.num1)

class B(A): # Child class - B inherits A , so B has properties of A
    def method_b(self,num2):
        self.num2 = num2
        print('Inside class B',self.num2)

obj1 = B()
obj1.method_a(23)
obj1.method_b(25)
