"""
Дан массив. Выведите сумму его значений, округленную до двух знаков после запятой, для следующей кусочно-заданной функции
y(x)={atan(x), x < 0 | 3∗x+4, x >= 0
"""
import numpy as np

n = 50  # int(input())
x = np.linspace(-np.pi / 2, 10, num=n)
y = np.where(x < 0, np.arctan(x), 3 * x + 4)
print(np.sum(y).round(2))
