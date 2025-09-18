# -*- coding: utf-8 -*-

# 테스트 케이스 수를 입력받습니다.
T = int(input())

# 각 테스트 케이스를 처리합니다.
for test_case in range(1, T + 1):
    num = list(map(int, input().split()))

    num.remove(min(num))
    num.remove(max(num))
    total = sum(num)
    result = total / len(num)
    print(f"#{test_case} {result:.0f}")

