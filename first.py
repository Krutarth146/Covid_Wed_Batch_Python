# Python is Dynamic, Interpreted Language

# int x = 10

x = 10

print(x)  # 10
print(90)

# Single Line Comment

'''
Multi
Line
Comment
'''

_1 = 90
_2 = 91

print(_1, _2,sep=' ')    # 90 91
print("Hello",end=' om ')
print("Covid Batch")


print('''
    Sarghasan Chokdi,
    Gnr, 300000
''')

x= 9000000000000000000000000
print(type(x))   # <class 'int'>

y = -80.78
print(type(y)) #  <class 'float'>

royal = "ROyal"   # <class 'str'>
royal1 = 'R'   # <class 'str'>
print(type(royal))  # <class 'str'>

w = True
print(type(w))   # <class 'bool'>

jk = 90 + 8j
print(type(jk))  # <class 'complex'>

print(jk + 80)   # (170+8j)


# Typecasting --> One Datatype to Another Datatype
# 1. Implicit Typecasting    2. Explicit Typecasting

r = 89
q = 90.21
print(r+q)  # 179.20999999  # Implicit Typecasting


j = True   # Bool ---> 1
w = 45   # int    
print(j+w)   # 46   # Implicit Typecasting


d1 = "90.67"
print(int(float(d1)))   # Gives Error   # Explicit Typecasting  # 90


import math

print(math.floor(90.9999999))
print(math.ceil(90.001))
print(math.ceil(99.000001))   # 100

print(round(float(d1)))   # 91

 
d1 = 90.80000000001
print(d1)
print(abs(d1))

print(-18//4)  # -5

list1 = [10,20,30,90.89, True, 78 + 9j,[[40,90],[10,20]], (10,20,30)]

print(list1)  # [10, 20, 30, 90.89, True, (78+9j), [[40, 90], [10, 20]], (10, 20, 30)]
print(type(list1))  # <class 'list'>

tupe = (10,10,20,30, 89.90, (10,20), {10,20,30,101,10,10})
print(tupe)  # (10, 10, 20, 30, 89.9, (10, 20), {10, 20, 101, 30}) <class 'tuple'>

dict = {'Name' : "Mehil", 'Roll' : 900, 'Address' : "Ahm"}
print(type(dict))   # <class 'dict'>

set2 = {10}
print(type(set2))  # <class 'set'>
set3 = set()
print(type(set3))  # <class 'set'>


# Input()
x1 = 90  # Int
x = int(input("Enter Value: "))  # str
y = int(input("Enter Value: "))  # str
print(x+int(y))   # 43

print(x,'+',y,'=',x+y)       # 21 + 23 = 44

# Arithmetic O/p

print(f"{x} + {y} = {x+y}")  # 21 + 23 = 44
print(f"{x} - {y} = {x-y}")  # 21 + 23 = 44
print(f"{x} * {y} = {x*y}")  # 21 + 23 = 44
print(f"{x} / {y} = {x/y}")  # 21 + 23 = 44    # Float 
print(f"{x} // {y} = {x//y}")  # 21 + 23 = 44  # Floor Division (int)
print(f"{x} % {y} = {x%y}")  # 21 + 23 = 44   # 1
print(f"{x} ** {y} = {x**y}")  # 21 + 23 = 44  # 625