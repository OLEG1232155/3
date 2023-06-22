#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

EPS = 1e-10

if __name__ == '__main__':

    x = float(input("Значение x = "))

    a = -x
    S, n = a, 1

    while math.fabs(a) > EPS:
        a *= ((-x ** 2) * (2 * n + 1)) / ((2 * n + 3) * (n + 1))
        S += a
        n += 1

    print(f"{(2 / math.pi) * S}")
