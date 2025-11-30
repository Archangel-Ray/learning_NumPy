"""
Вводится число n, затем двумерный целочисленный массив nxn. Выведите для каждого столбца этого массива True,
если в нем есть хотя бы одно число, отличное от 0.

В этой задаче запрещено использовать if
"""
import numpy as np

n, *arr = [list(map(int, x.split())) for x in open(0).readlines()]
n = n[0]
arr = np.array(arr)
print(np.any(arr != 0, 0))
