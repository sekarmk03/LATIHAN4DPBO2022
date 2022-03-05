from Vehicle import *

class Ship(Vehicle):
    def __init__(self):
        super().__init__()
        self.__countryOfManufacture = ""
        self.__machineType = ""
    
    def setCountryOfManuFacture(self, country):
        self.__countryOfManufacture = country

    def getCountryOfManufacture(self):
        return self.__countryOfManufacture
    
    def setMachineType(self, machineType):
        self.__machineType = machineType

    def getMachineType(self):
        return self.__machineType

    def sail(self, sail):
        print("The " + self.getName() + " ship " +
        ("is sailing.." if sail else "hasn't sailed yet."))

    def printShip(self, sail=False):
        print("Country\t\t: " + self.getCountryOfManufacture())
        print("Machine Type\t: " + self.getMachineType())
        self.sail(sail)