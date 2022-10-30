def myfunc(n):
    #return function
    return lambda a: a*n


mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))




