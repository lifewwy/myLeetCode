# Design a logger system that receive stream of messages along with its timestamps,
# each message should be printed if and only if it is not printed in the last 10 seconds.
#
# Given a message and a timestamp (in seconds granularity), return true if the message
# should be printed in the given timestamp, otherwise returns false.
#
# It is possible that several messages arrive roughly at the same time.
#
# Example:
#
# Logger logger = new Logger();
#
# // logging string "foo" at timestamp 1
# logger.shouldPrintMessage(1, "foo"); returns true;
#
# // logging string "bar" at timestamp 2
# logger.shouldPrintMessage(2,"bar"); returns true;
#
# // logging string "foo" at timestamp 3
# logger.shouldPrintMessage(3,"foo"); returns false;
#
# // logging string "bar" at timestamp 8
# logger.shouldPrintMessage(8,"bar"); returns false;
#
# // logging string "foo" at timestamp 10
# logger.shouldPrintMessage(10,"foo"); returns false;
#
# // logging string "foo" at timestamp 11
# logger.shouldPrintMessage(11,"foo"); returns true;

# 这道题让我们设计一个记录系统每次接受信息并保存时间戳，然后让我们打印出该消息，
# 前提是最近10秒内没有打印出这个消息。这不是一道难题，我们可以用哈希表来做。

import collections
class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__dq = collections.deque()
        self.__printed = set()

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp,
        otherwise returns false. The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        while self.__dq and self.__dq[0][0] <= timestamp - 10:
            self.__printed.remove(self.__dq.popleft()[1])

        if message in self.__printed:
            return False

        self.__dq.append((timestamp, message))
        self.__printed.add(message)

        return True

from collections import defaultdict
class Logger1(object):

    timeStoreLen = 10

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.timeToMessages = defaultdict(set)
        # maps a time to set of messages printed at that time

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp,
        otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        oldTimes = list( self.timeToMessages.keys() )

        # remove timestamps whare are too old
        for oldTime in oldTimes:
            if timestamp - oldTime >= self.timeStoreLen:
                del self.timeToMessages[ oldTime ]

        # printed same message recently?
        for oldTime in self.timeToMessages:
            if message in self.timeToMessages[oldTime]:
                return False

        self.timeToMessages[ timestamp ].add( message )
        return True



# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)

logger = Logger()
print(logger.shouldPrintMessage(1,'foo'))
print(logger.shouldPrintMessage(2,'bar'))
print(logger.shouldPrintMessage(3,'foo'))
print(logger.shouldPrintMessage(8,'bar'))
print(logger.shouldPrintMessage(10,'foo'))
print(logger.shouldPrintMessage(11,'foo'))
print(logger.shouldPrintMessage(12,'foo'))




















