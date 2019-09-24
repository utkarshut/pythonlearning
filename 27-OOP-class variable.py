# class variable common across instances

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


emp1 = Employee('ut', 'bhardw', 90)
emp2 = Employee('utk', 'bhardw', 10)

print(emp1.email)
print(emp2.email)
print(emp1.fullname())
print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)


print(emp1.__dict__)

print(Employee.__dict__)
