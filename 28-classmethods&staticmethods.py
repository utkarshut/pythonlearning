# class variable common across instances

import  datetime

class Employee:

    raise_amount = 1.04
    num_emp = 0

    def __init__(self, first, last, pay):
        self.first = first  # these instance variables
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_emp += 1

    def fullname(self):
        return '{}{}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)    #self.raise_amount

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount
        pass
    @classmethod
    def from_string(cls, empString):
        first, last, pay = empString.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return  True


emp1 = Employee('ut', 'bhardw', 90)
emp2 = Employee('utk', 'bhardw', 10)

Employee.set_raise_amt(1.05)
print(emp1.email)
print(emp2.email)
print(emp1.fullname())
print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)


print(emp1.__dict__)

print(Employee.__dict__)

emp_str = 'John-Doe-5777'
newEmp = Employee.from_string(emp_str)

print(newEmp.__dict__)

my_Day = datetime.date(2019, 10, 1)

print(Employee.is_workday(my_Day))

#In general, static methods know nothing about class state.
#They are utility type methods that take some parameters and
#work upon those parameters. On the other hand class
#methods must have class as parameter.