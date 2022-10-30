a = 0
b = 1

0,1,1,2,3,5,8,13,21,34
N = 10

for i in range(N):
    if i is not 0 and i is not 1:
        t = b
        b = a + b
        a = t
        print(b)
    else:
        print(i)
        


