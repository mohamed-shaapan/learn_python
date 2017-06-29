class Person:

    # ATTRIBUTES
    # ******************************************
    firstname = ""
    lastname = ""
    age=-1

    # CONSTRUCTOR
    # ******************************************
    def __init__(self, first, last, age):
        self.firstname = first
        self.lastname = last
        self.age=age

    # METHODS
    # ******************************************
    def displayFirstName(self):
        print ("first name", self.firstname)

    def displayLastName(self):
        print("last name", self.lastname)

    def displayAge(self):
        print("age", self.age)


# Inheritance
# *********************************************************************
# *********************************************************************
class Employee(Person):

    # ATTRIBUTES
    # ******************************************
    staffID=-1

    # CONSTRUCTOR
    # ******************************************
    def __init__(self, first, last, age, staffID):
        # super class
        super().__init__(first, last, age)
        # proprietary attributes
        self.staffID = staffID

    # METHODS
    # ******************************************
    def displayStaffID(self):
        print("staff ID", self.staffID)






















