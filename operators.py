# Assignment O/p   = += -= *= /= //= %= &= |= ^= <<= >>=
# (Low Priority)
x = 90

x+=10
print(x)  # x = x + 10   # 100

y = 800
y+=30  # 800 + 30 = 830
y/=3   # 830 / 3 = 276.6666
y-=204 # 72.6666
y%=2   # 0.6666

print(y)  # 0.6666

print(2**3**2 - 10 + 90 / 2)  #  547.0

# a = a + 1   # a += 1

# (Exp1 ? Exp2 : Exp3)  # Ternary

num1 = 9000
num2 = 8000
num3 = 900

if num1 > num2:
    if num1 > num3:
        print("Num1 is Greater")
    else:
        print("Num3 is Greater")
else:
    if num2 > num3:
        print("Num2 is Greater")
    else:
        print("Num3 is Greater")

# Compare 3 variables
print(( num1 if num1 > num3 else num3) if num1 > num2 else (num2 if num2 > num3 else num3))


'''
# printf("%d",num1 > num2 ? num1 : num2)

# a++

# a + b


# 2. Take 3 Subject Marks 1. Eng 2. Sci  3. Maths & Calculate Total , avg and Grade
100 - 80 ---> A Grade
60 - 80 ---> B Grade
40 - 60 ---> C Grade
Under 40 ---> D Grade

if any subject contains Under 40 marks then it will Fail

3. Take days as Input from User and FInd Total Years, Months, and remaining Days
# Ex. 400 ----> 1 Year, 1 Month, 5 Remaing Days

'''


for year in range(1999,3011):

    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        print(year,end=' ')
    

    