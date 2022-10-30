#open() function take two parameter .. filename and mode

#different modes
#================


#reading file
#f = open('mytemp.txt','r')
#data = f.read()
#print(data)
#f.close()



# writing to file
#data = [1.6,3.4,5.5,9.4]

#f = open('mytemp.txt','x')

#for value in data:
#    record = str(value)
#    f.write(record)
#    f.write("\n")

#f.close()


file = open("myfilee.txt",'w')
L = ["This is delhi\n","This is paris\n","This is London\n"]
file.writelines(L)
file.close()

#file2 = open("myfile.txt","a")#
#file2.write("Today\n")
#file2.close()

file1 = open("myfilee.txt", "r")
print("Output of Readlines after appending")
print(file1.read())
print()
file1.close()
