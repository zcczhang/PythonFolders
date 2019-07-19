# Author: CZ
# Time: 2019-07-07 23:43
import datetime as dt


# Inherit
class A:
    def __init__(self):
        self.x = 1

    def a(self):
        print(self.x)           # A().a(): 1


class B(A):
    def __init__(self):
        A.__init__(self)        # add some init val after inherit
        self.y = 2              # B().a(): 1


class B2:
    @staticmethod
    def b2():
        print(2)


class C(A, B2):
    def __init__(self):
        super().__init__()      # add some init val after inherit
        self.z = 3              # C().a(): 1;  C().b2(): 2


A().a()
B().a()
C().a()
C().b2()


class Capstr(str):      # inherited class str cannot be changed so we need to new
    def __new__(cls, strs):     # strs: variable introduced
        strs = strs.upper()     # rewrite the method
        return strs.__new__(cls, strs)


print(Capstr('a'))          # 'A'


class Newint(int):
    def __add__(self, other):
        return int.__sub__(self, other)     # rewrite the origin method int.__add__

    def __sub__(self, other):
        return int.__add__(self, other)

    def __radd__(self, other):              # inverse operation of add,
        return int.__sub__(self, other)     # calling when the first(left) num can't be operated


a = Newint('1')
b = Newint(2)

print(a+b, a-b, 1+b)         # -1 3, 1 (new) add, sub, radd


class D:
    def __str__(self):
        return 'd'

    def __repr__(self):
        return 'dd'


print(repr(D()))          # dd
print(D())                # d


class E:
    def __init__(self, e):
        self.e = e

    def gete(self):
        return self.e

    def sete(self, ee):
        self.e = ee

    def dele(self):
        del self.e

    x = property(gete, sete, dele)          # property: get, set, del


e1 = E('e0')
print(e1.x)         # e0
e1.x = 'E0'
print(e1.e)         # E0
del e1.x
try:
    print(e1.e)
except AttributeError as rsn:
    print(rsn)      # 'E' object has no attribute 'e'


class Celsius:
    def __init__(self, value = 0):
        self.value = value

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = float(value)


class Fahreheit:
    def __get__(self, instance, owner):
        return instance.cel * 1.8 + 32

    def __set__(self, instance, value):
        instance.cel = (float(value)-32)/1.8


class Temperature:
    cel = Celsius()
    fah = Fahreheit()


t = Temperature()
print(t.cel, t.fah)   # 0, 32.0
t.cel = 30
print(t.fah)          # 86.0
t.fah = 86
# fah->call Fahreheit()-> has '=' -> __set__-> 'instance' is t(Temperature)
# -> change t.cel
print(t.cel)          # 30.0


class Ranctangle:
    def __init__(self, wi, he):
        self.width = wi
        self.height = he

    def __setattr__(self, key, value):          # behaviour: self.key = value
        if key == 'square':
            self.width = value
            self.height = value
        else:                                   # without super(), 'll be dead loop,
            super().__setattr__(key, value)     # so get the father class

    def area(self):
        return self.width*self.height


r1 = Ranctangle(3, 4)
print(r1.area())
r1.square = 10
print(r1.width, r1.height, r1.area())          # 10 10 100 (attribute, attribute, function)


class Ranctangle2:
    def __init__(self, wi, he):
        self.width = wi
        self.height = he

    def __setattr__(self, key, value):
        if key == 'square':
            self.width = value
            self.height = value
        else:
            self.__dict__[key] = value

    def area(self):
        return self.width*self.height


r2 = Ranctangle2(3, 4)
r2.square = 2
print(r2.__dict__)              # {'width': 2, 'height': 2}
print(r2.area())                # 4


string = 'abcd'         # 'str' have the iteration itself
it = iter(string)
print(next(it))         # a
print(next(it))
print(next(it))
print(next(it))         # d
try:
    print(next(it))
except StopIteration:
    print('No Next')


class LeapYear:                 # iterator must have __iter__ and __next__, like a container
    def __init__(self):
        self.now = dt.date.today().year

    @ staticmethod
    def isleapyear(year):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return True
        else:
            return False

    def __iter__(self):
        return self

    def __next__(self):
        while not self.isleapyear(self.now):
            self.now -= 1

        temp = self.now
        self.now -= 1

        return temp


leapyears = LeapYear()
tmp = iter(leapyears)
print(next(tmp))            # 2016
print(next(tmp))            # 2012
leapyears2 = LeapYear()
for i in leapyears2:
    if i >= 2000:
        print(i)            # 2016, 12, 08, 04, 00
    else:
        break


def mygen():
    print("this is the generator！")
    yield 1     # like return, but the function is stoped now
    yield 2


g = mygen()
print()
print(next(g))
print()
print(next(g))


def fibs():             # generator exampl
    f1 = 0
    f2 = 1
    while True:
        f1, f2 = f2, f1+f2
        yield f1             # will not become the dead loop


for each in fibs():
    if each > 100:
        break
    print(each, end=' ')        # 1 1 2 3 5 8 13 21 34 55 89

