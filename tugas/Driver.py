from Person import *
from Job import *

class Driver(Person, Job):
    def __init__(self):
        super().__init__()
        self.__licenseId = ""
        self.__activeUntil = ""
        self.__vehicleType = ""
    
    def setLicenseId(self, licenseId):
        self.__licenseId = licenseId

    def getLicenseId(self):
        return self.__licenseId

    def setActiveUntil(self, activeUntil):
        self.__activeUntil = activeUntil

    def getActiveUntil(self):
        return self.__activeUntil

    def setVehicleType(self, vehicleType):
        self.__vehicleType = vehicleType

    def getVehicleType(self):
        return self.__vehicleType

    def printDriver(self, work):
        print("LicenseId\t: " + self.getLicenseId())
        print("Active\t\t: " + self.getActiveUntil())
        print("Vehicle\t\t: " + self.getVehicleType())
        print(self.getName() + " " + self.work(work))