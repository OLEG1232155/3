#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

if __name__ == '__main__':
    a = float(input("Введите произвольное действительное a: "))

    # sqrt(a - x) = x - 2
    # a - x = x^2 - 4x + 4
    # x^2 - 3x + 4 - a = 0
    # D = 9 - 4(4-a) = 9 - 16 + a = -7 + a >= 0
    # a >= 7
    # D = (3+math.sqrt(D)/(2a))

    D = -7 + a
    if D > 0:
        # если дискриминант больше 0
        x1 = (3 + math.sqrt(D)) / (2 * a)
        x2 = (3 - math.sqrt(D)) / (2 * a)
        print("Корни неравенства: ", x1, ' ', x2)
        print("Неравенство: ", math.sqrt(a - x1), " > ", x1 - 2)
        print("Неравенство: ", math.sqrt(a - x2), " > ", x2 - 2)
    if D == 0:
        # если дискриминант равен 0
        x1 = 3 / (2 * a)
        print("Корень неравенства: ", x1)
        print("Неравенство: ", math.sqrt(a - x1), " > ", x1 - 2)
    else:
        # если дискриминант меньше 0
        print("Нет корней или их бесконечное множество.")
