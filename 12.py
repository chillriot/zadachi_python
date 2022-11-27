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
b = []
c = []
for i in range(len(array)):
    if array[i] < 0:
        b.append(array[i])
    if array[i] > 0:
        c.append(array[i])
print(b)
print(c)