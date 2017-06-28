import math
import random

# DATA TYPES
# ***********************************************************
var_integer=123
var_long=123
var_float=123.321
var_complex=1+4j

# CASTING TO INTEGER
# ***********************************************************
str="123"
number_var=int(str)
#number_var=long(str)
number_var=float(str)
number_var=complex(str)

# NUMBER OPERATIONS
# ***********************************************************
number=-123
number=abs(number)
number=math.ceil(number)
number=math.floor(number)
number=max(range(1,200))
number=min(range(1,200))
number=random.choice(range(1,200))
number=random.random()

number=math.sqrt(number)
number=math.exp(number)
number=math.log(number, 2)
number=math.pow(number, 3)

number=math.sin(number)
math.cos(number)
math.tan(number)
math.asin(number); math.acos(number)

math.pi
math.e
