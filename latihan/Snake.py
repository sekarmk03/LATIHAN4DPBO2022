from Animal import *

class Snake(Animal):
    def __init__(self):
        super().__init__()
        self.__length = 0.0
        self.__isVenom = 0

    def setLength(self, length):
        self.__length = length

    def getLength(self):
        return self.__length

    def setIsVenom(self, isVenom):
        self.__isVenom = isVenom

    def getIsVenom(self):
        return self.__isVenom