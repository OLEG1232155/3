#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    for i in range(105, 999, 7):
        summ = 0
        for j in str(i):
            summ += int(j)
        if summ % 7 == 0:
            print(i)
