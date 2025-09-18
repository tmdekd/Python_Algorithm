# -*- coding: utf-8 -*-
from collections import Counter

# 테스트 케이스 개수 입력
T = int(input())
for t in range(1, T + 1):
    # 두 문자열 입력
    str1 = input()
    str2 = input()

    # str2의 각 문자의 빈도를 계산
    counter = Counter(str2)

    # str1의 문자 중 가장 많이 등장한 문자의 개수를 찾음
    max_count = 0
    for char in str1:
        if char in counter:
            max_count = max(max_count, counter[char])

    # 결과 출력
    print(f"#{t} {max_count}")
