import math
import random
import re
from datetime import datetime

print("Введите число N:")
N = int(input())
print("Введите число M:")
M = int(input())
print("Введите число K:")
K = int(input())
k1 = 2 - 1
P = k1 + M
array = [random.randint(1, 10) for i in range(N)]
print(array)
print(array[:k1] + array[P:])