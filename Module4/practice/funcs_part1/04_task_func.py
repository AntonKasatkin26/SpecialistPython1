# Даны координаты трех точек p1(x1; y1) p2(x2; y2) p3(x3; y3).
# Напишите функцию, проверябщую можно ли построить треугольник, соединив данные точки отрезками

def can_triangle(p1, p2, p3):
    # TODO: your code here
    pass


# Пример вызова функции
can_triangle((10, 12), (14, 18), (12, 12))

# Не забудьте протестировать вашу функцию


def can_triangle(p1, p2, p3):
    # TODO: your code here
    return (p1 + p2) > p3 or (p1 + p3) > p2
print(can_triangle((4, 4), (4, 4), (13, 13)))
