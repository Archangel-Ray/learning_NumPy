"""
Возьмем массу 10 пингвинов. Для одного пингвина по-прежнему не удалось собрать данные,
поэтому np.nan нужно заменить на среднее арифметическое по массе всех остальных пингвинов.
Выведите индексы пингвинов, масса которых лежит между 25 и 75 процентилями от массы.

Примечание. В тестирующей системе stepik установлен numpy версии 1.14,
поэтому для замены np.nan на среднее не удастся использовать np.nan_to_num()
"""
import numpy as np

body_mass_10 = np.array([3750., 3800., 3250.,   np.nan, 3450., 3650., 3625., 4675., 3475., 4250.])
average_value = np.round(np.nanmean(body_mass_10))
body_mass_10[np.isnan(body_mass_10)] = average_value
pr25 = np.percentile(body_mass_10, 25)
pr75 = np.percentile(body_mass_10, 75)
search_range = np.where((body_mass_10 >= pr25) & (body_mass_10 <= pr75))
print(*search_range)
