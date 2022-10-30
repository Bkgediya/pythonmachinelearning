class GrandFather():
    def __init__(self,grandFatherName):
        self.grandFatherName = grandFatherName



class Father(GrandFather):
    def __init__(self,fatherName,grandFatherName):
        self.fatherName = fatherName
        GrandFather.__init__(self,grandFatherName)

class Son(Father):
    def __init__(self,sonname,fatherName,grandFatherName):
        self.sonname = sonname
        Father.__init__(self,fatherName,grandFatherName)

    def print_name(self):
        print('Grandfather name :', self.grandFatherName)
        print("Father name :", self.fatherName)
        print("Son name :", self.sonname)
 

s1 = Son("Prince","RAMAN","LAL MANI")
print(s1.print_name())


f1 = Father("Good","Laimn")
print(f1.fatherName)
print(f1.grandFatherName)




