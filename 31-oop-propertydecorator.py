class Employee:
    raise_amt = 1.04

    def __init__(self, first, last):
        self.first = first  # these instance variables
        self.last = last

    @property
    def fullname(self):
        return '{}{}'.format(self.first, self.last)

    @property
    def email(self):
        return '{},{}Diii.com'.format(self.first, self.last)

    @fullname.setter
    def fullname(self,name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("delete names")
        self.first = None
        self.last = None




emp1 = Employee ('john', 'smith')

emp1.fullname ='utkarsh bhardwaj'   # we cant without setter


emp1.first = 'Jim'


print(emp1.email)

print(emp1.fullname)

del emp1.fullname

print(emp1.first)