class Person():
    def __init__(self):
        self.__nik = ""
        self.__name = ""
        self.__gender = 0
    
    def setNik(self, nik):
        self.__nik = nik

    def getNik(self):
        return self.__nik
    
    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setGender(self, gender):
        self.__gender = gender

    def getGender(self):
        return self.__gender

    def sleep(self, sleep):
        print(self.__name + (" is sleeping.." if sleep else " not sleeping."))

    def printPerson(self, sleep=False):
        print("Name\t\t: " + self.getName())
        print("NIK\t\t: " + self.getNik())
        print("Gender\t\t: " + ("Female" if self.getGender() else "Male"))
        self.sleep(sleep)