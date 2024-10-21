# -*- coding: utf-8 -*-  # 인코딩 설정
import math

list_a = input().split(", ")
list_b = [int(num) * math.pi * 2 for num in list_a]
for i in list_b:
    if i == list_b[-1]:
        print(f"{i:.2f}", end="")
    else:
        print(f"{i:.2f}", end=", ")