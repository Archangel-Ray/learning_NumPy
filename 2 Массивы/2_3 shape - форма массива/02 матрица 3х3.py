"""
Создать и вывести матрицу 3х3 со значениями от 0 до 8
"""
import numpy as np

arr = np.arange(0, 9)
arr = arr.reshape(3, -1)
print(arr)
