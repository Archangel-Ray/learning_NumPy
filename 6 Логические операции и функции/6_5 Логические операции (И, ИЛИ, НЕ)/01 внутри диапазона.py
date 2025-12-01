"""
Выведите булев массив, отвечающий на вопрос, какие из элементов данного массива больше low и меньше или равны up?
"""
import numpy as np

arr = np.array([9, 4, 5, 8, 9, 4])
low = int(input())
up = int(input())

print(np.logical_and(low < arr, arr <= up))
