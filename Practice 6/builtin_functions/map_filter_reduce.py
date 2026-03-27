from functools import reduce

numbers = [1, 2, 3, 4, 5]

# map: умножаем на 2
mapped = list(map(lambda x: x * 2, numbers))
print("map:", mapped)

# filter: только чётные
filtered = list(filter(lambda x: x % 2 == 0, numbers))
print("filter:", filtered)

# reduce: сумма
total = reduce(lambda x, y: x + y, numbers)
print("reduce:", total)