# Identity O/p

# is  is not

c = 90
z = 90

if c == z:
    print("c == z")
print(id(c))  # 3034686557200
print(id(z))  # 3034686557200
if c is z:
    print("c is z")


list1 = [10,20,30,40]
list2 = [10,20,30,40]

if list1 == list2:
    print("list1 == list2")   # list1 == list2


print(id(list1))   # 2731706734528
print(id(list2))   # 2731706885760
if list1 is list2:
    print("list1 is list2")

if 0 == False:
    print(True)

print("-----")


if 0 is False:
    print(True)
else:
    print("Fail")

# Loops 
# 1. Entry Control loops   --->  1. while   2. for

# 1. Intialization (start Point), 2. Condition (End point)  3. Flow (Incre / Decre) 

x = 10   # Intialization

while x <= 100:
    print(x,end=' ')
    x+=1

# 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100

x = 10   # Intialization

while x <= 100:
    print(x,end=' ')
    x+=2

# 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 52 54 56 58 60 62 64 66 68 70 72 74 76 78 80 82 84 86 88 90 92 94 96 98 100


# 65 to 25


_ = 65

while _ >= 25:
    print(_,end=' ')   # 65 64 63 62 61 60 59 58 57 56 55 54 53 52 51 50 49 48 47 46 45 44 43 42 41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25
    _-=1


print()


# Break & continue


i = 1        
while i<=4:    # i = 1
    j = 0
    while j<=4:  # j = 1
        if i == j:     # 1 == 1
            print("Hello")
            j+=1
            continue
            print("sdfnsdfns")
        print(j,end=' ')    # 
        j+=1
    print(i,end=' ')   
    i+=1
print(i)


# 0

i = 5

while i<=10:
    j=5
    while j<=i:
        if i <= j:
            j+=1
            continue
            print("Hello")
        j+=1
    i+=1

i = 1
while -5:
    j = 2
    while j<=4:
        if j == 4:
           break
        j+=1
    print(i)
    if i == 5:
        break
    i+=1
else:
    print("RUN Successfully")


# Print Reverse Number

num = 894   # 498

# while num > 0:
while num != 0:
    rem = num % 10     # rem = 4
    print(rem,end='')  # 4
    num = num // 10    # num = 89

print()

# Sum of Digits
num = 894   # 498
sum = 0

# while num > 0:
while num != 0:
    rem = num % 10     # rem = 4
    sum = sum + rem    # sum = 21
    num = num // 10    # num = 89

print(sum)   # 21


# Palindrome
num = 101   # 498
rev = 0
safe = num
# while num > 0:
while num != 0:
    rem = num % 10     # rem = 8
    rev = rev * 10 + rem    # sum = 498
    num = num // 10    # num = 0

print(rev)   # 101

if rev == safe:   # 101 == 101
    print("Palindrome")

# Armstrong
num = 8208   # 498
rev = 0
safe = num
# while num > 0:
while num != 0:
    rem = num % 10     # rem = 8
    rev = rev + rem ** len(str(safe))    # sum = 498
    num = num // 10    # num = 0

print(rev)   # 101

if rev == safe:   # 101 == 101
    print("Armstrong")


# Prime, Palindrome, Armstrong  ----->  1 to 10000