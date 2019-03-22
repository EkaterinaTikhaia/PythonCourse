a, b, c = int(input()), int(input()), int(input())
D = b**2 - 4*a*c
from math import sqrt 
if D < 0:
    print('нет корней')
if D == 0:
    print('корень уравнения х =', -b/(2*a))
if D > 0:
    print('корни уравнения: х1 =', (-b + sqrt(D))/(2*a), 'х2 =', (-b - sqrt(D))/(2*a))
