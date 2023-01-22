from math import sqrt

x1, y1 = input('Enter the first endpoint: ').split()
x2, y2 = input('Enter the second endpoint: ').split()
xlength = float(x1) - float(x2)
ylength = float(y1) - float(y2)
length = sqrt(xlength**2 + ylength**2)
print(f'The length of the line segment is: {length:.3f}')