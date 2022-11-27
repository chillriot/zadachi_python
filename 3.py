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
p = int(len(array) / 2)
for i in range(p):
    x = array[i]
    array[i] = array[i + p]
    array[i + p] = x
print("Ответ:")
print(array)