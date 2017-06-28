class Employee:

    # ATTRIBUTES
    # ******************************************
    empCount = 0

    # CONSTRUCTOR
    # ******************************************
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1


    # METHODS
    # ******************************************
    def displayCount(self):
        print ("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print ("Name : ", self.name, ", Salary: ", self.salary)


emp1 = Employee("mohamed", 100)