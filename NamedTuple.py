from collections import namedtuple

Color = namedtuple('C', ['red', 'green', 'blue'])
color = Color(55, 155, 255)
white = Color(112,113,114)

print(color.red)
print(color[0])
print(white.red,white.green,white.blue)
