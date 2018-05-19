# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.
#
# For example,
#
# MovingAverage m = new MovingAverage(3);
# m.next(1) = 1
# m.next(10) = (1 + 10) / 2
# m.next(3) = (1 + 10 + 3) / 3
# m.next(5) = (10 + 3 + 5) / 3

from collections import deque
class MovingAverage(object):
    def __init__(self,N):

        self.x = deque(maxlen=N)

    def next(self,d):
        self.x.append(d)
        return sum(self.x)/len(self.x)

m = MovingAverage(3)
print(m.next(1))
print(m.next(10))
print(m.next(3))
print(m.next(5))

