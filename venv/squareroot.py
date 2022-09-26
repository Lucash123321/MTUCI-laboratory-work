import math
a, b, c = map(int, [input() for _ in range(3)])
D = b**2 - 4 * a * c
if D > 0:
    print(f'x1 = {(-b + math.sqrt(D)) / (2 * a)}\nx2 = {(-b - math.sqrt(D)) / (2 * a)}')
elif D == 0:
    print(f'x1 = {-b / (2 * a)}')
else:
    print('Действительных корней нет')
