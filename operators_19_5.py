# Arithmetic, Assignment, Logical, Bitwise, Membership, Identity, Comparison

# Bitwise  & | ^ << >>

print(78 & 256)  # 0
print(21 | 24)  # 29
print(21 ^ 24)  # 13
print(21 >> 2)  # 5
print(89 << 4)  # 1424

# Logical  (and, or, not)

print(~90)  # -91
print(~(-25))  # 24

num = 80

if num % 7 == 0 or num % 5 == 0:
    print("Divisible By 5 or 7")


# Linear Search

need = int(input("Enter Number: "))

list1 = [90,52,89,12,45,77]

# for _ in list1:
#     if _ == need:
#         print("Element is Found")
#         break
# else:
#     print("Not Found")


# Membership o/p   in, not in 
if need in list1:
    print("Element is Found")
else:
    print("Not Found")


l1 = [1,2,3,4,56,1,2,3,4]
unique = []


for i in l1:
    if i not in unique:
        unique.append(i)

print(unique)


# Comparison o/p  == != < > <= >=