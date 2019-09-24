message = 'football'

if message == 'cricket':
    print('cricket')
elif message == 'football':
    print('football')
else:
    print('nothing')

# object identity -> is  and or not


a = [1, 2, 3]
b = [1, 2, 3]

print(id(a))
print(id(b))

print(a is b)

# false valuees: False [] {} () numeric 0 None ''
