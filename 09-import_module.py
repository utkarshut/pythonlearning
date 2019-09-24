# import mymodule as mm
from mymodule import find_index  # or for all function and variable import *
import sys
import random
import math
import datetime
import calendar
import os

courses = ['math', 'hindi', 'english', 'physics']

# print(mm.find_index(courses, 'english'))
print(find_index(courses, 'english'))

print(sys.path)

randomchoice = random.choice(courses)

print(randomchoice)

print(datetime.date.today())

print(calendar.isleap(2022))
# export path  in  nano ~/bash_profile

print((os.getcwd()))

print(os.__file__)
