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
P = 0
M = 0
for i in range(len(array)):
    if array[i] > 0:
        P += array[i]
    if array[i] < 0:
        M += array[i]
print(P)
print(-M)
if P > -M:
    array.append(-(M + P))
if P < M:
    array.append(-(P + M))
print(array)