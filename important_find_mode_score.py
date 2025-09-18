# -*- coding: utf-8 -*-

# 최빈수 찾기 (기출문제)

# 테스트 케이스 수를 입력받습니다.
T = int(input())

# 각 테스트 케이스를 처리합니다.
for test_case in range(1, T + 1):
    case_number = int(input())  # 테스트 케이스 번호
    scores = list(map(int, input().split()))  # 학생들의 점수 목록

    # 0점부터 100점까지의 빈도를 저장할 리스트 초기화
    frequency = [0] * 101

    # 각 점수의 빈도를 계산합니다.
    for score in scores:
        frequency[score] += 1

    # 최대 빈도수를 가진 점수를 찾습니다.
    max_frequency = max(frequency)
    mode_score = 0

    # 빈도수가 가장 높고 점수가 가장 큰 값을 찾습니다.
    for score in range(101):
        if frequency[score] == max_frequency:
            mode_score = score

    # 출력 형식에 맞춰 출력합니다.
    print(f"#{test_case} {mode_score}")
