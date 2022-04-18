x = (1, 2, 4)
y = [1, 2, 4]
print(x, type(x))
print(y, type(y))
(a, b, c) = x
print(a, b, c, type(a))
t=(a,b,c)
print("t:",t,type(t))
y[0] = 99
print(y, type(x))
i = y.index(2)
print(i)
t = tuple(range(10,20,3))+tuple(range(10))
print(t)
i= t.index(16)
print(i)
#
t=str(t)
print(t,type(t))
