class Animal:
    def __init__(self):
        self.__name = ""
        self.__hasTail = 0
        self.__skinType = ""
        self.__foodType = ""
    
    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setHasTail(self, hasTail):
        self.__hasTail = hasTail

    def getHasTail(self):
        return self.__hasTail

    def setSkinType(self, skinType):
        self.__skinType = skinType

    def getSkinType(self):
        return self.__skinType

    def setFoodType(self, foodType):
        self.__foodType = foodType

    def getFoodType(self):
        return self.__foodType

    def eat(self):
        print(self.__name + " is eating..")

    def sleep(self):
        print(self.__name + " is sleep..")