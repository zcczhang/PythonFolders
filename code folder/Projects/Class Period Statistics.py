# Author: CZ
# Time: 2019-07-09 12:56

import datetime
import time
from easygui import*


begin_over = buttonbox(msg='Class Begin or Over', choices=['Begin', 'Cancel'])
if begin_over == 'Begin':
    start_time = datetime.datetime.now()
    start_time2 = time.localtime()
    buttonbox(msg='In Class...', choices=['Over'])
else:
    start_time = 0
    start_time2 = 0
    exit(0)

end_time = datetime.datetime.now()
end_time2 = time.localtime()

st = time.strftime("%H:%M:%S", start_time2)
en = time.strftime("%H:%M:%S", end_time2)
time_period = (end_time - start_time).total_seconds()
c = time_period/60

if start_time != 0:
    with open('Class Periods Record.txt', 'a+') as rf:
        d = time.strftime("%Y.%m.%d", time.localtime())
        rf.writelines('{}: class from {} to {}, {} min'.format(d, st, en, c)+'\n')


def total_time():
    with open('Class Periods Record.txt', 'r') as f:
        times = []
        allt = 0
        for each_line in f:
            (sth, t) = each_line.split(', ')
            (n, u) = t.split(' ')
            times.append(n)
        for i in range(len(times)):
            allt += eval(times[i])
    return allt


print(total_time())

