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
for i in range(len(array)):
    if array[i] == 0 and i != 0:
        b = array[i - 1] + array[i - 2]
        array[i] = b
print(array)