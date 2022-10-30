class MyError(Exception):

    def __init__(self,value):
        self.value = value


    def __str__(self):
        return (repr(self.value))



try:
    raise(MyError(3*6))

except MyError as error:
    print('A new Error occured',error.value)


#error with multiple inheritance


class Error(Exception):
    pass

class ZeroDivision(Error):
    pass

try:
    num = int(input("Enter a number : "))
    if num == 0:
        raise ZeroDivision

except ZeroDevision:
    print("Input value is zero try again")



class TransitionError(Error):
    def __init__(self,prev,nex,msg):
        self.prev = prev
        self.nex = nex
        self.msg = msg


try:
    raise(TransitionError(2,36,"Not allowed"))
except TransitionError as error:
    print("Exception occured",error.prev)
