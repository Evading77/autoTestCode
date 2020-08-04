from functools import reduce


def f(s):
    return s[0].upper()+s[1:].lower()

a=['admin','LISA','insA']
b=list(map(f,a))
print(b)

def prod(L):
    return reduce(f,L)
def f(x,y):
    return x*y
a=[1,2,3,4,5]
b=prod(a)
print(b)

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]
def by_score(t):
    return t[1]
#key作用于列表上的每一个元素，练习里就是每个tuple都传入了key，而不是直接传入L
print(sorted(L,key=by_name))
print(sorted(L,key=by_score,reverse=True))