class Father():
    fatherName=""

    def father(self):
        print(self.fatherName)



class Mother():
    motherName = ""

    def mother(self):
        print(self.motherName)


class Son(Mother,Father):
    def parents(self):
        print("And the father name  is : ",self.fatherName)
        print("mother name is : ",self.motherName)


s = Son()
s.fatherName = "RAMESH"
s.motherName = "LALI"
s.parents()
