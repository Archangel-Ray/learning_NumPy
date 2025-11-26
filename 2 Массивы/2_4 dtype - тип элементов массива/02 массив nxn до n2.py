"""
Вводится целое положительное число n. Сгенерируйте и выведите массив вещественных чисел размерностью nxn,
с последовательно расположенными числами от 1 до n**2
"""
import numpy as np

n = int(input())

arr = np.arange(1, n ** 2 + 1, dtype=float)
arr = arr.reshape(n, n)
print(arr)
