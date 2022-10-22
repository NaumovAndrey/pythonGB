# Вложенные циклы list complication
from urllib3.connectionpool import xrange

print([x + y for x in [1, 5] for y in [10, 20]])

# Состояние проверено на 1-й петле
print([x + y for x in [1, 2, 3] if x > 2 for y in [3, 4, 5]])

# Состояние проверено на 2-й петле
print([x + y for x in [1, 2, 3] for y in [3, 4, 5] if x > 2])

# Условие проверено, если зацикленные числа нечётные
print([x for x in xrange(10) if x % 2 == 0])
