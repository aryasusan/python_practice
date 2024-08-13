# 3 main concepts:
#     - class
#     - object
#     - referance
#
# class:
#     - blueprint or base model
# object:
#     - the pattern designed using class
# reference:
#     - operations used in object

# example:
# TV - lg,samsung,sony,impex,mi
# TV- class
# lg,samsung,sony ,etc - object
# on/off,volume up/down,channel up/down - reference

# phone - samsung,iphone,oppo,vivo
# phone-class
# brands- object
# call,camera,text - reference

class Person:
    def reading(self):
        print("reading a book")
    def writing(self):
        print("writing a book")

# each functions written in a class is called method
# self is an instance variable/ dynamic variable -
# inst/dyn variable is a variable that can be reused in multiple methods
object1 = Person()
object1.reading()
object1.writing()

object2 = Person()
object2.writing()

# object1 has references reading and writing
#  object2 has only writing

