
#single exception
#===================
try:
    10 * (1/0)
except:
    print("The calculation failed")

#multiple exception
#   ==============

try:
    print(x)
except NameError:
    print("x is not defined")
except:
    print("something gone wrong")

#finally block

try:
    print(x)
except NameError:
    print("x is not defined")
except:
    print("something gone wrong")
finally:
    print("The programe is finished")


try:
    f = open("myfile.txt")
    f.write("lorum ipsum")
except:
    print("something went wrong then writing to the file")
finally:
    f.close()
