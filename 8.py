import math
import random
import re
from datetime import datetime

print("Введите число N:")
N = int(input())
i = 0
print("Ввод массива")
array = []
while i != N:
    print("Введите число: ")
    answer = input()
    array.append(int(answer))
    i = i + 1
print("Вы ввели:")
print(array)
arr = []
i = 0
while i < N:
    if array[i] == 0:
        i = i + 1
        continue
    else:
        arr.append(array[i])
        i = i + 1
print(arr)