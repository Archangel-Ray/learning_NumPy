"""
Проводились соревнования по программированию, всего было 5 заданий. Первый этап был отборочным
и если участник не набрал пороговый балл (5), то он мог принимать дальше участие, но не мог стать призером.
А призерами становились участники, набравшие больше 7 баллов за каждое из оставшихся заданий. Выведите баллы призеров.

Формат входных данных
В первой строке вводится n - количество участников. Затем двумерный целочисленный массив размерностью nx5

Формат выходных данных
Программа должна вывести двумерный целочисленный массив - баллы призеров
"""
import numpy as np

# n, *arr = open(0).readlines()
# n = int(n)
# arr = np.array([list(map(int, x.split())) for x in arr])
n = 5
arr = np.array([[8, 8, 8, 8, 8], [2, 9, 7, 8, 8], [2, 9, 6, 9, 3], [5, 9, 9, 6, 6], [5, 4, 2, 1, 9]])
first_stage = np.greater(arr[:, 0], 4)
awardees = arr[first_stage]
minimum_score_of_awardees = np.min(awardees[:, 1:], 1)
prize_stage = np.greater(minimum_score_of_awardees, 7)
winners = awardees[prize_stage]
print(n, arr, first_stage, awardees, minimum_score_of_awardees, prize_stage, winners, sep='\n')
