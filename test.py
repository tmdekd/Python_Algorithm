# -*- coding: utf-8 -*-  # 인코딩 설정

list_a = input().split(", ")
sorted_list = sorted(list_a)

for i in sorted_list:
    if i == sorted_list[-1]:
        print(i, end="")
    else:
        print(i, end=", ")