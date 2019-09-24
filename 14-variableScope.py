# LEGB
# Local enclosing global built in

x = 'global x'


def test():
    # y ='local y'
    # print (y)
    x = 'local x'
    print(x)


test()
print(x)

import builtins

print(dir(builtins))

# def min():
#     pass


a = min([1, 4, 6, 3, 6])

print(a)


def outer():
    x = 'outer x'

    def inner():
        nonlocal x
        x = 'inner x'
        print(x)

    inner()
    print(x)


outer()
