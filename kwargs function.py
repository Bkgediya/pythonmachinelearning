#**kwargs function

#A keyword argument is where you provide a name to
#the variable as you pass it into the function.

#programme to illustrate keyword argument

def myFunc(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} == {value}")

        
myFunc(first='Geeks', mid='for', last='Geeks')



def myFun(arg1, **kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


myFun("Hi", first='Geeks', mid='for', last='Geeks')

# *args and **kwargs to call a function

def nomFunc(arg1,arg2,arg3):
    print("arg1:",arg1)
    print("arg2:",arg2)
    print("arg3:",arg3)



args = ("Geeks","for","Geeks")

nomFunc(*args)

kwargs = {"arg2": "Geeks","arg1": "for", "arg3": "Geeks"}
nomFunc(**kwargs)


# Now we can use both *args ,**kwargs
# to pass arguments to this function :
def myFun(*args, **kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)
 
 

myFun('geeks', 'for', 'geeks', first="Geeks", mid="for", last="Geeks")



#*args and **kwargs to set values of object



class Car():
    def __init__(self,*args):
        self.speed = args[0]
        self.color = args[1]

audi = Car(200,'red')
bmw = Car(250,'black')
mb = Car(190,'white')

print(audi.color)
print(bmw.speed)

class CarNew():
    def __init__(self,**kwargs):
        self.speed = kwargs['s']
        self.color = kwargs['c']


audi = CarNew(s=200,c='red')
bmw = CarNew(s=250,c='black')
mb = CarNew(s=190,c='white')

print(audi.color)
print(bmw.speed)



class Person():

    def __init__(self,name):
        self.name = name

    def getName(self):
        return self.name

    def isEmployee(self):
        return False;


class Employee(Person):
    def isEmployee(self):
        return True;



per = Person('Geeks1')
print(per.getName(),per.isEmployee())

emp = Employee('hello')

print(emp.getName(),emp.isEmployee())




    

