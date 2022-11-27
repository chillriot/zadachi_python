import math
import random
import re
from datetime import datetime

print("Введите число M:")
M = int(input())
print("Введите число K:")
K = int(input())
print("Введите число P:")
P = int(input())
array = []
print("Введите число, или 'stop', чтобы закончить ввод: ")
answer = input()
while str(answer) != "stop":
    array.append(int(answer))
    print("Введите число, или 'stop', чтобы закончить ввод: ")
    answer = input()
print("Вы ввели:")
print(array)
for i in range(K, K + M):
    x = array[i]
    array[i] = array[P - K + i]
    array[P - K + i] = x
print(array)