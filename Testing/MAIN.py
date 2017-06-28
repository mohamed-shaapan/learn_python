import Advanced.modules
import data_types.objects

# MAIN METHOD
"""
term = int(input("enter term : "))

result=Advanced.modules.fib(term)

print("fib(",term,") = ",result)
"""

# CREATE OBJECTS
emp1 = data_types.objects.Employee("mohamed", 100)
emp1.empCount=200
getattr(emp1, 'age')
setattr(emp1, 'age', 8)