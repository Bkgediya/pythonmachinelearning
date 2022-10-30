#The word polymorphism means having many forms. In programming,
#polymorphism means the same

#function name (but different signatures) being used for different types.



def add(x,y,z = 0):
    return x + y +z


print(add(2,3))
print(add(2,3,9))


#Polymorphism with class methods


class India():
    def capital(self):
        print("New Delhi")

    def language(self):
        print("hindi")

    def type(self):
        print("Developing")


class USA():
    def capital(self):
        print("Washington")

    def language(self):
        print("english")

    def type(self):
        print("developed")

ind = India()
usa = USA()

for country in (ind,usa):
    country.capital()
    country.language()
    country.type()


#polymorphism with inheritance


class Bird():
    def intro(self):
        print("there are many type of birds")

    def flying(self):
        print("birds can fly")

class Sparrow(Bird):
    def flying(self):
        print("sparrow can fly")

class Ostrich(Bird):
    def flying(self):
        print("Ostrich")

bird = Bird()
sparrow = Sparrow()
ostrich = Ostrich()

bird.intro()
bird.flying()


sparrow.intro()
sparrow.flying()

ostrich.intro()
ostrich.flying()


#polymorphism with function and objects

def func(obj):
    obj.capital()
    obj.language()
    obj.type()

obj_ind = India()
obj_usa = USA()
  
func(obj_ind)
func(obj_usa)
