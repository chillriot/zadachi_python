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
count = 0
for i in range(len(array) - 1):
    if array[i] == 0 and array[i + 1] == 0:
        count = 1
if count == 0:
    print("Двух подряд нулей нету")
else:
    print("Два подряд нуля есть")