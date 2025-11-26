"""
Создать и вывести матрицу 5х5 с пятёрками по диагонали, элементы должны иметь вещественный тип данных
"""
import numpy as np

arr = np.zeros((5, 5), float)
for i in range(5):
    for j in range(5):
        if i == j:
            arr[i, j] = 5

print(arr)

# решение автора
arr2 = np.zeros((5, 5))
i = np.arange(5)
arr2[i, i] = 5
print(arr2)
