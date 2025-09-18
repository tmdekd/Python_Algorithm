# 소인수분해 문제
# 소인수분해 과정이 가능한 이유는 각 소인수를 최대한 나눈 후 다음 소인수로 넘어가는 방식

# -*- coding: utf-8 -*-
# 테스트 케이스 개수 입력
T = int(input())

# 소인수 리스트 (2, 3, 5, 7, 11)
factors = [2, 3, 5, 7, 11]

# 각 테스트 케이스 처리
for test_case in range(1, T + 1):
    # N 값 입력 받기
    N = int(input())
    counts = []  # 각 소수의 지수를 저장할 리스트

    # 각 소인수에 대해 지수 계산
    for factor in factors:
        count = 0  # 현재 소인수의 지수를 0으로 초기화
        while N % factor == 0:  # 해당 소인수로 나눌 수 있는 동안 반복
            N //= factor
            count += 1
        counts.append(count)  # 계산한 지수를 리스트에 추가

    # 출력 형식에 맞추어 결과 출력
    print(f"#{test_case} {' '.join(map(str, counts))}")
