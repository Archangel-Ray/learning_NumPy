"""
Сгенерируйте одномерный массив x целых чисел от -3 до 3 не включительно. Вычислите для каждого
xi  функцию y(x) = 5∗∣x3∣ , результат округлите до двух знаков после запятой
"""
import numpy as np

arr = np.arange(-3, 3)
arr = 5*np.absolute(np.cbrt(arr))
arr = np.round(arr, 2)
print(arr)
