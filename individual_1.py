#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    m = int(input("Введите номер месяца: "))

    if m < 7:
        print("Первое полугодие")
    else:
        print("Второе полугодие")

    if m == 2:
        print("28 дней в месяце.")
    elif m % 2 == 1:
        print("31 дней в месяце.")
    else:
        print("30 дней в месяце.", )
