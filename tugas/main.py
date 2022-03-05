from Ship import *
from Airplane import *
from Driver import *

print("------------------")
print("Input Vehicle Data")
print("------------------")
menu = ["Vehicle", "Ship", "Airplane"]

print("Select One")
for i in range(0, len(menu)):
    print(str(i + 1) + ". " + menu[i])
choose = int(input("-> "))

n = int(input("Number of " + menu[choose-1] + ": "))
vehicles = []

for i in range(0, n):
    print("Input " + menu[choose-1] + " " + str(i + 1))
    vehicleName = input("> " + menu[choose-1] + " Name: ")
    fuelType = input("> Vuel Type: ")
    maxPass = input("> Max Passengers: ")
    prodYear = int(input("> Prod Year: "))
    type = input("> Type: ")
    vehicleObj = Vehicle()
    if choose == 2:
        countryOfManufacture = input("> Country of Manufacture: ")
        machineType = input("> Machine Type: ")
        vehicleObj = Ship()
        vehicleObj.setCountryOfManuFacture(countryOfManufacture)
        vehicleObj.setMachineType(machineType)
    elif choose == 3:
        wingsLength = float(input("> Wings Len: "))
        serviceType = input("> Service Type: ")
        vehicleObj = Airplane()
        vehicleObj.setWingsLength(wingsLength)
        vehicleObj.setServiceType(serviceType)
    vehicleObj.setName(vehicleName)
    vehicleObj.setFuelType(fuelType)
    vehicleObj.setMaxPassengers(maxPass)
    vehicleObj.setProdYear(prodYear)
    vehicleObj.setType(type)
    vehicles.append(vehicleObj)

print("--------------")
print("Input Job Data")
print("--------------")
workerId = input("> Worker Id: ")
company = input("> Company Name: ")
position = input("> Position: ")
field = input("> Field: ")
salary = input("> Salary: ")
jobObj = Job()
jobObj.setWorkerId(workerId)
jobObj.setCompanyName(company)
jobObj.setPosition(position)
jobObj.setField(field)
jobObj.setSalary(salary)

print("-----------------")
print("Input Person Data")
print("-----------------")
nik = input("> NIK: ")
name = input("> Name: ")
print("> Gender: ")
print("1. Male")
print("2. Female")
gender = int(input("> ")) - 1
person = Person()
isDriver = True if input("> A Driver? (y/n) ") == "y" else False
if isDriver:
    licenseId = input("> License Id: ")
    active = input("> Active Until: ")
    vehicleType = input("> Vehicle Type: ")
    person = Driver()
    person.setLicenseId(licenseId)
    person.setActiveUntil(active)
    person.setVehicleType(vehicleType)
person.setNik(nik)
person.setName(name)
person.setGender(gender)

print("\n# Output Vehicle Data #")
for i in range(0, len(vehicles)):
    print("> " + menu[choose-1] + str(i + 1))
    move = True if (i % 2 == 0) else False
    vehicles[i].printVehicle(move)
    if choose == 2:
        sail = True if (i % 2 == 0) else False
        vehicles[i].printShip(sail)
    elif choose == 3:
        fly = True if (i % 2 == 0) else False
        vehicles[i].printAirplane(fly)

print("\n# Output Job Data #")
jobObj.printJob(work=False)

print("\n# Output Person Data #")
person.printPerson(sleep=False)
if isDriver:
    person.printDriver(work=True)