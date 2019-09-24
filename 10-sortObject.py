class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({},{}.${})'.format(self.name, self.age, self.salary)


e1 = Employee("JOHN1", 37, 70000)
e2 = Employee("JOHN2", 31, 70008)
e3 = Employee("JOHN3", 34, 70009)

employee = [e1, e2, e3]


def age_sort(emp):
    return emp.age


s_emp = sorted(employee, key=age_sort)

print(s_emp)

s_emp1 = sorted(employee, key=lambda e: e.salary)

print(s_emp1)

from operator import attrgetter

s_emp2 = sorted(employee, key=attrgetter('age'))

print(s_emp2)
