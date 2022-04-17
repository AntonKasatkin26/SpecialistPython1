# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.

def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


ab = distance(1, 1, 2, 9)
bc = distance(2, 9, 3, 7)
ac = distance(1, 1, 3, 7)


def min_dist(*args):
    min_dist = args[0]
    for el in args:
        if el < min_dist:
            min_dist = el
    if min_dist == ab:
        res = "AB"
    elif min_dist == bc:
        res = "BC"
    else:
        res = "CD"
    return res


print("Самый короткий отрезок:", min_dist(ab, bc, ac))  # Выводим название отрезка, например “АС”.
