class Job():
    def __init__(self):
        self.__workerId = ""
        self.__companyName = ""
        self.__position = ""
        self.__field = ""
        self.__salary = ""

    def setWorkerId(self, workerId):
        self.__workerId = workerId

    def getWorkerId(self):
        return self.__workerId

    def setCompanyName(self, companyName):
        self.__companyName = companyName

    def getCompanyName(self):
        return self.__companyName
    
    def setPosition(self, position):
        self.__position = position

    def getPosition(self):
        return self.__position

    def setField(self, field):
        self.__field = field

    def getField(self):
        return self.__field

    def setSalary(self, salary):
        self.__salary = salary

    def getSalary(self):
        return self.__salary

    def work(self, work):
        return "is working.." if work else "not yet working."

    def printJob(self, work=False):
        print("Worker Id\t: " + self.getWorkerId())
        print("Company Name\t: " + self.getCompanyName())
        print("Position\t: " + self.getPosition())
        print("Field\t\t: " + self.getField())
        print("Salary\t\t: " + self.getSalary() + " IDR")
        self.work(work)