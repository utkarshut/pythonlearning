class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first  # these instance variables
        self.last = last
        self.pay  = pay

    @property
    def fullname(self):
        return '{}{}'.format(self.first, self.last)

    @property
    def email(self):
        return '{},{}Diii.com'.format(self.first, self.last)
