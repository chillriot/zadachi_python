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
i = 0
j = 0
while i < (len(array)-1):
    while j < (len(array)-1):
        temp = array[j+1]
        array[j+1] = array[j]
        array[j] = temp
        j = j + 1
    j = 0
    i = i + 1
print(array)