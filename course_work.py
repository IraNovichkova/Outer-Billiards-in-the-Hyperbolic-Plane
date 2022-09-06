from PIL import Image
from PIL import ImageDraw
from math import sqrt
import sys
sys.setrecursionlimit(10000)

# настраиваем размер холста, рисуем единичную окружность и треугольник с центром в нуле
# так как вблизи начала координат прямые диска пуанкаре очень похожи на евклидовы прямые, то стороны треугольника нарисованы через евклидовы прямые
# размер треугольника можно менять, меняя значение r
width = 1001
height = 1001
R_x, R_y = int(width / 2), int(height / 2)
image = Image.new("RGB", (width, height))
draw = ImageDraw.Draw(image)
center = complex(R_x, R_y)
r = 70
pol = [(R_x+r, R_y), (R_x - r/2, R_y - sqrt(3) * r / 2),
       (R_x - r/2, R_y + sqrt(3) * r / 2)]
draw.rectangle((0, 0, width - 1, height - 1), fill='white', outline='white')
draw.ellipse((0, 0, width - 1, height - 1), fill=(255, 255, 0), outline='yellow')


# координаты пикселя переводим в координаты точки единичной окружности
def complex_coordinates(z):
    return complex((z.real - R_x) / R_x, -(z.imag - R_y) / R_y)


# обратное отображение: координаты точки единичной окружности переводим в координаты пикселя
def reverse(z):
    return round(z.real * R_x + R_x), round(-z.imag * R_y + R_y)


# функция, результатом которой является отражение комплексной точки z относительно комплексной точки v
def reflection(z, v):
    answer = (-2 * v + z * (1 + (abs(v))**2)) / \
             (2 * v.conjugate() * z - (1 + (abs(v))**2))
    return complex(round(answer.real, 4), round(answer.imag, 4))


# координаты вершин треугольника в диске пуанкаре
z1 = complex_coordinates(complex(pol[0][0], pol[0][1]))
z2 = complex_coordinates(complex(pol[1][0], pol[1][1]))
z3 = complex_coordinates(complex(pol[2][0], pol[2][1]))


# уравнение прямой диска пуанкаре проходит через 2 точки x и y
# функция проверяет местоположение точки z: точка выше прямой, ниже или лежит на прямой, проходящей через точки x и y
def find_segment(z, x, y):
    M_x = (x - y) / (1 - y.conjugate() * x)
    a, b = M_x.real, M_x.imag
    phi = complex((a ** 2 - b ** 2) / (a ** 2 + b ** 2),
                  2 * a * b / (a ** 2 + b ** 2))
    function1 = phi * (z.conjugate() - y.conjugate()) * (1 - y.conjugate() * z)
    function2 = (z - y) * (1 - y * z.conjugate())
    if abs(function1 - function2) < 1e-2 / 5:
        return 'the point is on the line'
    elif (function1 - function2).real + \
            (function1 - function2).imag - 1e-2 / 5 < 0:
        return 'выше'
    else:
        return 'ниже'


# треугольник делит диск пуанкаре на 3 области, в каждой из которых точки отражаются относительно одной вершины треугольника.
# функция проверяет, в какой из трёх областей лежит точка и возвращает вершину треугольника, относительно которой нужно отражать точку z. если точка z лежит на луче, на котором отображение не определено, функция выводит 'stop'
def area(z):
    a_12 = find_segment(z, z1, z2)
    a_13 = find_segment(z, z3, z1)
    if a_12 == 'выше':
        if a_13 == 'выше':
            return z1
        elif a_13 == 'the point is on the line' and z.real > z1.real:
            pass
        else:
            return z3
    elif a_12 == 'ниже':
        a_23 = find_segment(z, z2, z3)
        if a_23 == 'ниже':
            return z2
        elif a_23 == 'the point is on the line' and z.imag < z3.imag:
            pass
        else:
            return z3
    elif z.real > z1.real:
        return z3
    return 'stop'


# применяем левый внешний бильярд к точке z count раз. если точка попала на луч, на котором отражение не определено, функция прекращает свою работу
def left_billiards(z, z_i, count):
    draw.ellipse((reverse(z)[0] - 0.1, reverse(z)[1] - 0.1,
                  reverse(z)[0] + 0.1, reverse(z)[1] + 0.1),
                 fill='black', outline='black')
    if z_i == 'stop':
        return
    elif count != 0:
        a_i = reflection(z, z_i)
        return left_billiards(a_i, area(a_i), count - 1)


# основной цикл, в котором на лучи, отмеченые синим в файле readme.md, действует отображение левого бильярда. можно менять количество итераций, меняя число 500 на какое-то другое (1, 2, 50, 100, 500, 5000) в функции left_billiards(z, area(z), 800)
for i in range(0, width):
    for j in range(0, height):
        z = complex_coordinates(complex(i, j))
        if abs(z) < 1:
            if find_segment(z, z1, z2) == 'the point is on the line' \
                    and z.real > z1.real or \
                find_segment(z, z2, z3) == 'the point is on the line' \
                    and z.imag > z2.imag or \
                find_segment(z, z3, z1) == 'the point is on the line' \
                    and z.real < z3.real:
                left_billiards(z, area(z), 800)


draw.polygon(pol, fill='red')
image.save("outer_billiard.png", "PNG")
image.show()
