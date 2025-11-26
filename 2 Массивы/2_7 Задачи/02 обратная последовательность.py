"""
Вводятся целые положительные числа n и m. Создайте и выведите целочисленный массив размерностью n x m
c значениями от 1 до n*m в обратном порядке
"""
import numpy as np

n = int(input())
m = int(input())
print(np.arange(n * m, 0, -1).reshape(n, m))
