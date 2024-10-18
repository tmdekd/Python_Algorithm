# -*- coding: utf-8 -*-  # 인코딩 설정

list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(filter(lambda x : x % 2 == 0, list_a)))