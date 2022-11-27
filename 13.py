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
        P += 1
    if array[i] < 0:
        M += 1
if P > M:
    for i in range(M, P):
        array.append(random.randint(-10, -1))
if P < M:
    for i in range(P, M):
        array.append(random.randint(1, 10))
print(array)