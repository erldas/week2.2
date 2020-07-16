a = ['Sanya', 'Roma', 'Oleg', 'Dima']
b = 'Na obed priglasheny tolko 2'
print(b)
d = 'Sorry, mest malo ,sednya bez tebya, '
v = a.pop()
print(d+v)
n= a.pop(2)
print(d+n)

c = 'Jdu tebya v 23-00, '
print(c+a[0])
print(c+a[1])


del a[0]
del a[0]
print(a)
