tag = 'h1'
text = 'this is xyz'

sentance = '<{0}>{1}</{0}>'.format(tag, text)

print(sentance)

person = {'name': 'john', 'age': 17}
list = ['john', 17]

sentance1 = 'my name is {0[name]} and age is  {0[age]}'.format(person)
sentance2 = 'my name is {0[0]} and age is  {0[1]}'.format(list)

print(sentance1)
print(sentance2)


class Person():
    def __init__(self, name, age):
        self.name = name;
        self.age = age;


p1 = Person('john', 17)

sentance3 = 'my name is {0.name} and age is  {0.age}'.format(p1)

print(sentance3)

# two digit

for i in range(10):
    sentance = 'the value is {:02}'.format(i)
    print(sentance)

pi = 3.14556

sentance4 = 'pi is {:.3f}'.format(pi)  # 3 decimal point

print(sentance4)

sentance5 = '1 MB is {:,.2f}'.format(1000 ** 2)

print(sentance5)

import datetime

my_date = datetime.datetime(2019, 10, 2, 12, 35, 00)

print(my_date)

sentance6 = '{:%B %d ,%Y}'.format(my_date)

print(sentance6)

sentance7 = '{0:%B %d ,%Y} month {0:%A} days{0:%j}'.format(my_date)

print(sentance7)
