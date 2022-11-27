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
for i in range(0, len(array), 2):
    x = array[i]
    array[i] = array[i + 1]
    array[i + 1] = x
print("Ответ:")
print(array)
