# -*- coding: utf-8 -*-
# 부분집합 문제
from itertools import combinations

T = int(input())  # 테스트 케이스 수 입력
for t in range(1, T + 1):
    n, k = map(int, input().split())  # 부분집합 원소 개수 n, 합 k 입력

    # 집합 A 생성
    A = list(range(1, 13))  # 1부터 12까지의 숫자를 원소로 가진 집합

    count = 0  # 조건에 맞는 부분집합의 개수
    # 부분집합 탐색 (combinations 사용)
    # 입력받은 A에서 길이가 n인 모든 조합을 반환
    for subset in combinations(A, n):
        if sum(subset) == k:
            count += 1

    # 결과 출력
    print(f"#{t} {count}")
