def triangle(n):
    L=[1]
    yield(L)
    for i in range(n-1) :
        L=[1]+[L[x]+L[x+1] for x in range(len(L)-1)]+[1]
        yield L

a=triangle(5)
for b in a :
    print(b)