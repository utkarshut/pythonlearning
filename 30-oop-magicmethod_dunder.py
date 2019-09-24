class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first  # these instance variables
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{}{}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amt)  # self.raise_amount

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)


    def __str__(self):
        return  '{} - {}'.format(self.fullname(), self.email)


    def __add__(self, other):
        return  self.pay + other.pay

    def __len__(self):
        return  len(self.fullname())


emp1 = Employee('ut', 'bhardw', 90)

emp2 = Employee('utfe', 'bhardw', 90)


print(emp1)

print(repr(emp1))  # emp1.__repr__()
print(str(emp1))


print(int.__add__(1, 3))
print(str.__add__('1', '3'))

print(emp1 + emp2)


print(len('test'))
print('test'.__len__())


print(len(emp1))
