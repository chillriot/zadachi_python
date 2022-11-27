import math
import random
import re
from datetime import datetime

print("Введите число N:")
N = int(input())
j = 0
print("Ввод массива")
array = []
while j != N:
    print("Введите число: ")
    answer = input()
    array.append(int(answer))
    j = j + 1
print("Вы ввели:")
print(array)
arr = []
i = 0
while i < N:
    if array[i] < 0:
        arr.append(array[i])
        arr.append(int(math.pow(array[i], 2)))
        i = i + 1
    else:
        arr.append(array[i])
        i = i + 1
print(arr)