from collections import namedtuple

#more readable than other dict li
Color = namedtuple('Color', ['red', 'green', 'blue'])

color = Color(55, 155, 255)

print(color[0])

print(color.red)

dict_color = {'red': 55, 'green': 155, 'blue': 255}

color1 = Color(255, 255, 255)

print(d)