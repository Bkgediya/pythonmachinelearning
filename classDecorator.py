#class emthod are bound to class not the object of class

class ClassDecorator():
    @classmethod
    def fun(cls,arg1,arg2):
        print("hello")


#return ->  class method for function




#A static method does not receive an implicit first argument.
#A static method is also a method that is bound to the class and not the object of the clas


class StaticMethod():
    @staticmethod
    def fun(arg1,arg2):

        return #static method for function fun


from datetime import date

class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age

 # a class method to create a Person object by birth year.
    @classmethod
    def fromBirthYear(cls,name,year):
        return cls(name,date.today().year-year)

# a static method to check if a Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18

person1 = Person('mayank',21)
person2 = Person.fromBirthYear('mayank',1996)

print(person1.age)
print(person2.age)

print(Person.isAdult(22))

print(Person.fromBirthYear('mayank',1996))

