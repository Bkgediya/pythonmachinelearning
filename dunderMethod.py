
#example
#__init__, __add__, __len__

class String():

    def __init__(self,string):
        self.string = string

    def __repr__(self):
        return 'Object : {}'.format(self.string)

    def __add__(self,other):
        return self.string + other


if __name__ == '__main__':
    string1 = String("Hello")

#print address of string object 
    print(string1 + ' Geeks ')


#__getitem__

class A:
    def __init__(self,item):
        self.item = item

    def __getitem__(self,index):
        return self.item[index]

a = A([1,2,3,4,5])
print(f"first item : {a[0]}")
print(f"second item : {a[1]}")
print(f"third item : {a[2]}")



#__setitem__


class setItemExample:
    def __init__(self,item):
        self.item = item
    def __setitem__(self,index,value):
        self.item[index] = value

setItem = setItemExample([1,2,3])
setItem[1] = 4

print(f"Items after setting: {setItem.item}")


#__repr__
class RepoExample():
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def __repr__(self):
        return f"{self.a},{self.b},{self.c}"

rep = RepoExample(1,2,3)
print(rep)


#__len__

class LenExample:
    def __init__(self,item):
        self.item = item

    def __len__(self):
        return len(self.item)


len_instance = LenExample([1,2,3])
print(len(len_instance))



