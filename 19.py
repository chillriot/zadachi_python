import math
import random
import re
from datetime import datetime

array = []
print("Введите число, или 'stop', чтобы закончить ввод: ")
answer = input()
while str(answer) != "stop":
    array.append(int(answer))
    print("Введите число, или 'stop', чтобы закончить ввод: ")
    answer = input()
print("Вы ввели:")
print(array)
b = 0
c = 0
d = 0
for i in range(len(array)):
    if array[i] % 3 == 0 and array[i] != 0:
        b += 1
print("1/3:", b)
for i in range(len(array)):
    if array[i] % 2 == 0:
        c += array[i]
        d += 1
        f = c / d
print("+/2:", f)
array.insert(0, b)
array.append(f)
print(array)