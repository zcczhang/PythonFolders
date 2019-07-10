# Author: CZ
# Time: 2019-07-07 23:43


# Inherit
class A:
    def __init__(self):
        self.x = 1

    def a(self):
        print(self.x)


class B(A):
    def __init__(self):
        A.__init__(self)
        self.y = 2


class B2:
    @staticmethod
    def b2():
        print(2)


class C(A, B2):
    def __init__(self):
        super().__init__()
        self.z = 3


A().a()
B().a()
C().a()
C().b2()


class Capstr(str):      # inherited class str cannot be changed so we need to new
    def __new__(cls, strs):     # strs: variable introduced
        strs = strs.upper()     # rewrite the method
        return strs.__new__(cls, strs)


print(Capstr('a'))


