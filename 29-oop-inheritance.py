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


class Developer(Employee):
    raise_amt = 1.01

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        #Employee().__init__(self, first, last, pay) #else way
        self.prog_lang=prog_lang

    pass

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees =employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())



emp1 = Developer('ut', 'bhardw', 90, 'JAVA')
emp2 = Developer('utk', 'bhardw', 10, 'Python')

print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)
print(emp2.prog_lang)
#print(help(Developer))

mgr1 = Manager('sd', 'smits', 90000, [emp1])
mgr1.add_emp(emp2)

mgr1.print_emps()

print(isinstance(mgr1, Employee))

print(issubclass(Manager, Developer))

print(issubclass(Manager, Employee))

print(isinstance(mgr1, Developer))