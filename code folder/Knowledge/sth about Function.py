import math


def add(a, b):
    print(a, b)
    return a+b


add(5, 6)               # 5 6
print(add(3, 4))        # 3 4 newline 7
temp = add(7, 8)        # 7 8
print(' ')
temp                    # not print
print(temp)             # 15
print(' ')


def test(*a):
    print('the length is: ', len(a))
    print('the third parameter is: ', a[2])


test(1, 2, 3, 4, 5, 6)
print(' ')


count = 5


def globalvariable():
    global count        # if 'count' chaneges in the function, all 'count' change
    count = 7
    count = 10          # if no global, changes only work in the function
    print(count)


globalvariable()        # 10
print(count)            # 10, if no global, will be 5
print(' ')


# Nested Function
def t0():
    print('t0 is using')

    def t1():
        print('t1 is using')
    t1()


t0()


# closure
def x1(a):
    def y1(b):
        return a*b          # 'a' not changed, so a don't needs nonlocal
    return y1


temp1 = x1(5)                # type(temp1) is Function
print(x1(5)(8), temp1(8))


def m1():
    num1 = 5

    def m2():
        nonlocal num1
        num1 *= num1        # 'num1' changed, so num1 needs nonlocal
        return num1
    return m2()


print(m1())

# other function
print(list(filter(lambda num: math.sqrt(num) % 1 == 0, range(100))))    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
"""
after filter, getthe num which %1 == 0 from [0,100) <=> all perfec square
"""

print(list(filter(lambda num: num % 2, range(10))))                     # [1, 3, 5, 7, 9]
"""
after filter, get the num which %2 != 0  from [0,10) <=> all odd num
iteration in function so that the function returns True
"""
print(list(map(lambda num: num ** 2, range(10))))   # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
"""
map(function, iteration), iteration in function 
"""
print(' ')


# recursion
def fbnc(n):
    if n == 1 or n == 2:            # F(1) = F(2) = 1
        return 1
    else:
        return fbnc(n-1)+fbnc(n-2)  # F(n) = F(n-1)+F(n-2)


print('The result is %d' % fbnc(20))


# Tower of Hanoi: function: move n plates from x to z
def hanoi(n, x, y, z):
    if n == 1:
        print(x, '->', z)
    else:
        hanoi(n-1, x, z, y)     # move n-1 plates from x->y
        print(x, '->', z)       # move the last plate from x to z
        hanoi(n-1, y, x, z)     # move n-1 plates from y to z


hanoi(3, 'x', 'y', 'z')

try:
    raise TypeError
except TypeError:
    print('no error')            # no error


# while else
def maxfactor(n):
    t = n//2
    while t > 1:
        if n % t == 0:
            print('%d is the max factor of %d' % (t, n))
            break
        t -= 1
    else:
        print('%d is a prime' % n)


maxfactor(4)






