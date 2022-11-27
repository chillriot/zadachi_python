import math
import random
import re
from datetime import datetime

print("Введите число N:")
N = int(input())
array = [random.randint(-1000, 1000) for i in range(N)]
print(array)
S = sum(array)
print("Сумма элементов: " + str(S))
j = 0
for i in range(N):
    if array[i] >= 0:
        j += 1
print("Положительных элементов: " + str(j))
array.insert(0, S)
array.insert(1, j)
print(array)