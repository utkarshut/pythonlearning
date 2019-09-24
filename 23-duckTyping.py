
#pythonic code, they mean that the code uses Python idioms well, that it's natural or displays fluency
#in the language. In other words, it means the most widely adopted idioms that are adopted by the Python community


#EAFP duck typing and easier to ask forgiveness than permission


class Duck:

    def quack(self):
        print('quack..')

    def fly(self):
        print('flap flap')

class Person:

    def quack(self):
        print('I m quacking like duck')

    def fly(self):
        print('I m flapping')

def quackandfly(thing):

    #not duck typed(non-pythonic)

    if isinstance(thing,Duck):
        thing.quack()
        thing.fly()
    else:
        print('this has to be duck')

    print()


def quackandfly1(thing):

    #LBYL(non-pythonic)
    if hasattr(thing,'quack'):
        if callable(thing.quack):
            thing.quack()


    print()

def quackandfly2(thing):

    #pythonic
    thing.quack()
    thing.fly()

    print()


def quackandfly3(thing):

    #pythonic
    try:
        thing.quack()
        thing.fly()
        thing.bark()
    except AttributeError as e:
        print(e)

    print()


d = Duck()
quackandfly(d)

p = Person()

quackandfly(p)


person = {'name': 'John', 'age': 23 }

try:
    print("I m {name}. I m {age} and job {job}".format(**person))
except KeyError as e:
    print(("missing {}".format(e)))

list =[1,2]

try:
    print(list[3])
except IndexError:
    print('index not found')

# IO errror in file handling
