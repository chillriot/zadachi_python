import math
import random
import re
from datetime import datetime

print("Введите число N:")
N = int(input())
print("Введите число K:")
K = int(input())
print("Введите число P:")
P = int(input())
i = 0
print("Ввод первого массива")
array1 = []
while i != N:
    print("Введите число: ")
    answer = input()
    array1.append(int(answer))
    i = i + 1
print("Вы ввели:")
print(array1)
i = 0
print("Ввод второго массива")
array2 = []
while i != K:
    print("Введите число: ")
    answer = input()
    array2.append(int(answer))
    i = i + 1
print("Вы ввели:")
print(array2)
print(array1[:K] + array2 + array1[K:])