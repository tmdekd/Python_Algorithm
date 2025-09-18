# -*- coding: utf-8 -*-

# 테스트 케이스 수를 입력받습니다.
T = int(input())

for test_case in range(1, T + 1):
    # N일 동안의 매매가를 입력받습니다.
    N = int(input())
    prices = list(map(int, input().split()))

    # 오른쪽부터 최대 가격을 추적하여 최대 이익을 계산합니다.
    max_price = 0
    total_profit = 0

    # 오른쪽에서 왼쪽으로 탐색
    for price in reversed(prices):
        if price > max_price:
            max_price = price
        else:
            total_profit += max_price - price

    # 결과 출력
    print(f"#{test_case} {total_profit}")
