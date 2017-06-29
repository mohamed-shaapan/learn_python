import data_types.objects

#'''

# SUPER CLASS
p1 = data_types.objects.Person("mohamed", "shaapan", 100)
p1.displayFirstName()
p1.age


# SUBCLASS
emp1 = data_types.objects.Employee("mohamed", "shaapan", 100, 5)
emp1.displayStaffID()

