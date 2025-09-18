# -*- coding: utf-8 -*-
# 최빈값 구하기 : 기출문제
from collections import Counter

# 테스트 케이스 수 입력
for t in range(1, int(input()) + 1):
    case = int(input())
    scores = map(int, input().split())

    counter = Counter(scores)
    result_value = max(counter.values())
    result_key = 0

    for key, value in counter.items():
        if value == result_value:
            # 최빈값 중 가장 큰 수여야 하기 때문에
            if result_key < key:
                result_key = key

    print(f"#{case} {result_key}")