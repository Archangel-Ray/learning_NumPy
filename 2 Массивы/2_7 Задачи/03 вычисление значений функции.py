"""
Вычислите значение функции y=3∗x2+2∗x+3 для n точек в диапазоне [0, 3]
"""
import numpy as np

n = int(input())
arr = np.linspace(0, 3, n)
# я понимаю, что перебор массива не хорошая идея, но не представляю как это решить
arr = np.array([3 * x ** 2 + 2 * x + 3 for x in arr])
print(arr)

# вариант автора
x = np.linspace(0, 3, n)
print(3 * x ** 2 + 2 * x + 3)
