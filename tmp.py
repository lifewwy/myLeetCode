

from collections import defaultdict
class Logger1(object):

    def __init__(self):
        self.__x = defaultdict(set)

    def shouldPrintMessage(self, timestamp, message):
        for i in list(self.__x.keys()):
            if timestamp-i >=10:
                del self.__x[i]

        for i in self.__x:
            if message in self.__x[i]:
                return False

        self.__x[timestamp].add(message)

        return True

logger = Logger1()
print(logger.shouldPrintMessage(1,'foo'))
print(logger.shouldPrintMessage(2,'bar'))
print(logger.shouldPrintMessage(3,'foo'))
print(logger.shouldPrintMessage(8,'bar'))
print(logger.shouldPrintMessage(10,'foo'))
print(logger.shouldPrintMessage(11,'foo'))
print(logger.shouldPrintMessage(12,'foo'))
