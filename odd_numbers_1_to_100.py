# -*- coding: utf-8 -*-

# 1부터 100까지의 숫자 중 홀수만 출력하는 코드
for num in range(1, 101, 2):  # 2부터 100까지 2씩 증가하며 반복
    if num == 99:  # 마지막 숫자인 99일 때
        print(num, end="")
    else:
        print(num, end=", ")  # 각 숫자를 출력하고 공백으로 구분
