# Author: CZ
# Time: 2019-07-08 14:44 
"""
    Dice
"""
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter


class Dice:
    """
        Get and Combine Some Dice Rolling Result
    """
    def __init__(self, times, faces, num):
        self.time = times
        self.range = faces
        self.num = num

    # a dice rolling result array
    def rollarr(self):
        return np.random.randint(1, self.range+1, size=self.time)

    # N Dice rolling result arr
    def getndice(self):
        arr = np.zeros((self.num, self.time))
        for i in range(self.num):
            arr[i] = Dice(self.time, self.range, 1).rollarr()
        return arr

    # Sum of N dice rolling result respectively list
    def getandcombine(self):
        ta = self.getndice()
        arrsum = np.zeros((1, self.time))
        for i in range(self.num):
            arrsum += ta[i]
        return arrsum

    # Times of each face (sum) appeared diction
    def gett(self):
        return dict(sorted(Counter(self.getandcombine()[0]).items()))

    #  frequencies of each face (sum) appeared diction
    def getf(self, timedict):
        fd = timedict
        for i in timedict:
            fd[i] /= self.time
        return fd

    # get scatter plot
    def getscatterplt(self):
        for i in range(self.num):
            plt.scatter(range(self.time), self.getndice()[i], alpha=0.6, label='Dice%d' % (i+1))
        plt.xlabel('Rolling Times', fontsize=15)
        plt.ylabel('Rolling Result', fontsize=15)
        plt.title('Scatterplot of %d Dice Rolling Result' % self.num, fontsize=15)
        plt.legend(loc='upper right')
        plt.show()

    # get histogram plot
    def gethistplt(self):
        plt.hist(self.getandcombine().tolist(), bins=range(self.num, self.num*self.range+2),
                 normed=1, edgecolor='black', rwidth=0.8)
        tick_pos = np.arange(self.num, self.num*self.range+1)
        plt.xticks(tick_pos+0.5, tick_pos)   # time consuming
        plt.xlabel('Sum of every Dice', fontsize=15)
        plt.ylabel('Frequency', fontsize=15)
        plt.title('Histogram of %d Dice Rolling %d Times' % (self.num, self.time), fontsize=15)
        plt.show()


def main():
    dice = Dice(10000, 6, 3)
    dice.gethistplt()


if __name__ == '__main__':
    main()

