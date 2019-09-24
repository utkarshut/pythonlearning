class Employee:
    def __init__(self, first, last, pay):
        self.first = first     # these instance variables
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    def fullname(self):
        return '{}{}'.format(self.first, self.last)


emp1 = Employee('ut', 'bhardw', 90)
emp2 = Employee('utk', 'bhardw', 000)



print(emp1.email)
print(emp2.email)
print(emp1.fullname())