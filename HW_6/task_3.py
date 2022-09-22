# Найти расстояние между двумя точками пространства(числа вводятся через пробел)

import math
coords = '1 3 2.5 2 5.7 6' 
dist = list(map(lambda x: float(x), coords.split(' ')))
sq = lambda x2, x1: (x2-x1)**2
print(round(math.sqrt((sq(dist[3], dist[0]) + sq(dist[4], dist[1]) + sq(dist[5], dist[2]))), 2))

