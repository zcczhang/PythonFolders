#####################
print('eval: input string -> number')
str1 = input()
if str1.isdigit():
    a = eval(str1)+1
    print(a)
    print(' ')
#####################
print('indexing')
str2 = '0123456789'
print(str2[3])      # 3
print(str2[-1])     # 9
print(str2[1:2])    # 1
print(str2[:2])     # 01
print(str2[0:7:3])  # 036(012 345 67) 3 is the step length
print(' ')
#####################
print('calculation')
print(2**3)     # <=> 2^3 = 8
print(7//3)     # only quotient (= 2)
print(' ')
#####################
print('if')
x, y = 4, 5
m = x if x < y else y
print(m)    # 4
print(' ')
#####################
print('for')
a = ['123', '12', '12345', '1']
for i in a:
    print(i, len(i))    # len: length of the str
print(' ')

for i in range(1, 11, 2):   # 2:step length; list(range(5)) = [0,1,2,3,4]
    print(i)                # print: 1,3,5,7,9
print(' ')

for i in range(10):
    if i % 2 != 0:
        print(i)
        continue    # if i is odd, i will not +2 anymore, back to 'for'
    i += 2
    print(i)
print(' ')

for i in range(10):
    if i % 2 != 0:
        print(i)
        break       # if i is odd, 'for' will stop
    i += 2
    print(i)
print(' ')
#####################
print('list')
list1 = ['a', 'b', 'c', 'd', 'e', 'f']
list2 = list1[:]
# copy list1[:] and is independent; if using list2 = list1, list2 will change if list1 changes later
temp = list1[0]
list1[0] = list1[1]
list1[1] = temp
print(list1)           # [b,a,c,d,e,f]

list1.remove('a')      # remove 'a'
print(list1)
del list1[2]
print(list1)           # delete 'd'
list1.pop()            # delete the last str in list1
print(list1)
list1.pop(0)           # delete 'b'
print(list1)
print(list2[1:4])      # [b,c,d]

list3 = [123, 'bcd']
list4 = [234, 'abc']
print(list3 > list4)                # False
list4 = [234, 'abz']
list5 = [234, 'bcd', ['abc', 'cde']]
print(list4 < list5)                # True: compare the position of alphabet
print('cde' not in list3 + list5)   # True
print(list5[2][1])                  # cde
list4.insert(1, 456)
print(list4)                        # [234,456,'abz']

list4.reverse()
print(list4)                        # ['abz',456,234]
list6 = [1, 4, 2, 8, 5, 7]
list6.sort()
print(list6)                        # [1,2,4,5,7,8]
list6.sort(reverse=True)            # [8,7,5,4,2,1]
print(list6)
list6.append(0)
print(list6)                        # [8, 7, 5, 4, 2, 1, 0]
print()
#####################
print('tuple')
tuple1 = 1, 2, 4, 5, 6, 7
print(type(tuple1), 8*(8,))               # it's tuple; (8,8,8,8,8,8,8,8)
tuple1 = tuple1[:2] + (3,) + tuple1[2:]   # characteristic of tuple：','; only way to add sth
print(tuple1)                             # (1, 2, 3, 4, 5, 6, 7)
print()
#########################
str3 = 'fghdefghijkfgh'
print(str3.index('fgh', 3, 12))     # 5: first occur at 5, from 3 to 12
print(str3.count('fgh', 3, len(str3)))    # 2: 'fgh' occurs twice from 3 to the end
print(str3.capitalize())            # initial capitalizes
print(str3.casefold())              # initial casefold
print(str3.find('233', 3, 12))      # same as index but if can't find, return -1q
print(str3.strip('fgh'))            # delete the 'str' or ' ' at the beginning or the end
str4 = 'I love you'
print(str4.replace('you', 'U'))
print(str4.split())                 # ['I', 'love', 'U']
print(str4.split('o'))              # ['I l', 've y', 'u']
str5 = 'aaabbbcccddd'
print(str5.translate(str.maketrans('ac', 'ef')))  # eeebbbfffddd
print(str5.replace('ac', 'ef'))                   # not change
#####################
print('format')
print('{0} love {a} {c}'.format('I', a='U', c='2'))             # I love U 2
print('{1} love {0} {2}'.format('I', 'U', '2'))                 # U love I 2: {num} num is idex
print('{0:.2f}{1}'.format(27.65678656, 'GB'))                   # .2f: 2 decimal: 27.66GB
print('%o' % 10, '%x' % 10)                                     # 10 in duodecimal number system and hexadecimal
print('This is %s' % 'string', '%d+%d' % (1, 1))                # This is string 1+1
print('%f' % 27.3987, '%E' % 1397898, '%.2e' % 21231.123123)    # 27.398700 1.397898E+06 2.12e+04

a = 'I love U'
b = [1, 4, 2, 8, 5, 7]
a = list(a)
print(a)    # ['I', ' ', 'l', 'o', 'v', 'e', ' ', 'U']
print(max(a))   # v
print(sorted(b), list(reversed(b)))  # [1, 2, 4, 5, 7, 8] [7, 5, 8, 2, 4, 1]
print(list(enumerate(b)))   # [(0, 1), (1, 4), (2, 2), (3, 8), (4, 5), (5, 7)]: has the index
c = ['a', 'b', 'c', 'd']
print(list(zip(b, c)))  # [(1, 'a'), (4, 'b'), (2, 'c'), (8, 'd')]
print(' ')
#########################
print('diction')
dict1 = {'a': '1', 'b': '2', 'c': '3'}      # one-one mapping
print(dict1['c'])                           # 3
dict2 = dict((('a', '1'), ('b', '2'), ('c', '3')))
print(dict2 == dict1)                       # True
dict3 = dict(a='1', b='2', c='3')
print(dict3 == dict2 == dict1)              # True
dict3['d'] = 4
print(dict3)    # {'a': '1', 'b': '2', 'c': '3', 'd': 4}
dict4 = {}
dict4 = dict4.fromkeys(range(4), 'good')
print(dict4)    # {0: 'good', 1: 'good', 2: 'good', 3: 'good'}
for i in dict4.keys():
    print(i)    # 0//1//2//3
for i in dict4.values():    # return all values in 'key-values pairs'
    print(i)    # 'good' prints four times
for i in dict4.items():
    print(i)    # (0, 'good')(1, 'good')(2, 'good')(3, 'good')
print(dict4.get(0))     # good
dict4.clear()
print(dict4)    # {}
print(' ')
######################
print('Set')
print(type(dict4))           # <class 'dict'>
print(type({1, 2, 3, 4}))    # <class 'set'>
set1 = set([1, 2, 3, 4, 5])  # list becomes set
set1.add(6)
set1.remove(5)
print(set1, 1 in set1, '1' in set1)    # {1, 2, 3, 4, 6} True False
set2 = frozenset([1, 2, 3])  # cannot add, remove, etc.
