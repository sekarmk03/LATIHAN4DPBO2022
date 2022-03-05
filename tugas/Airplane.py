from Vehicle import *

class Airplane(Vehicle):
    def __init__(self):
        super().__init__()
        self.__wingsLength = 0
        self.__serviceType = ""

    def setWingsLength(self, wingsLength):
        self.__wingsLength = wingsLength

    def getWingsLength(self):
        return str(self.__wingsLength)

    def setServiceType(self, serviceType):
        self.__serviceType = serviceType
    
    def getServiceType(self):
        return self.__serviceType

    def fly(self, fly):
        print("The " + self.getName() + " plane " +
        ("is flying.." if fly else "hasn't flown yet."))

    def printAirplane(self, fly=False):
        print("Wings L\t\t: " + self.getWingsLength() + " meters")
        print("Service\t\t: " + self.getServiceType())
        self.fly(fly)