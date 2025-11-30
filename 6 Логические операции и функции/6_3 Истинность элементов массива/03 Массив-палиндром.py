"""
Дан одномерный массив. Выведите True, если массив и его перевернутая версия равны, иначе False
"""
import numpy as np

arr = np.array([1, 1, 0, 1, 1])

print(np.all(arr == arr[::-1]))
