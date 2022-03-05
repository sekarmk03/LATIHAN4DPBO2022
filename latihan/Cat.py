from Animal import *

class Cat(Animal):
    def __init__(self):
        super().__init__()
        self.__color = ""
        self.__breed = ""
    
    def setColor(self, color):
        self.__color = color

    def getColor(self):
        return self.__color

    def setBreed(self, breed):
        self.__breed = breed

    def getBreed(self):
        return self.__breed

    