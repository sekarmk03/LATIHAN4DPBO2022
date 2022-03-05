from datetime import date

class Vehicle:
    def __init__(self):
        self.__name = ""
        self.__fuelType = ""
        self.__maxPassengers = ""
        self.__prodYear = 0
        self.__age = 0
        self.__type = ""
        self.__todaysDate = date.today()
    
    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setFuelType(self, fuelType):
        self.__fuelType = fuelType
    
    def getFuelType(self):
        return self.__fuelType
    
    def setMaxPassengers(self, maxPassengers):
        self.__maxPassengers = maxPassengers
    
    def getMaxPassengers(self):
        return self.__maxPassengers

    def setProdYear(self, prodYear):
        self.__prodYear = prodYear
        self.setAge()

    def getProdYear(self):
        return str(self.__prodYear)

    def setAge(self):
        self.__age = self.__todaysDate.year - self.__prodYear

    def getAge(self):
        return str(self.__age)
    
    def setType(self, type):
        self.__type = type

    def getType(self):
        return self.__type
    
    def move(self, move):
        print("Vehicle is " + ("moving.." if move else "idle."))

    def printVehicle(self, move):
        print("Name\t\t: " + self.getName())
        print("Fuel Type\t: " + self.getFuelType())
        print("Max Pass\t: " + self.getMaxPassengers() + " people")
        print("Prod Year\t: " + self.getProdYear())
        print("Age\t\t: " + self.getAge() + " years")
        print("Type\t\t: " + self.getType())
        self.move(move)
    