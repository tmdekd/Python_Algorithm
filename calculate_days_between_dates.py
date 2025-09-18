# 두 날짜 간의 일수를 계산
# -*- coding: utf-8 -*-

days_in_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

T = int(input())
for i in range(1, T + 1):
    month_1, day_1, month_2, day_2 = map(int, input().split())
    result = 0

    # 같은 달이면 바로 계산
    if month_1 == month_2:
        result = day_2 - day_1 + 1
    else:
        # 첫 번째 달의 남은 일수 계산
        result += days_in_month[month_1] - day_1 + 1

        # 첫 번째 달과 두 번째 달 사이의 모든 달의 일수를 더하기
        for month in range(month_1 + 1, month_2):
            result += days_in_month[month]

        # 두 번째 달의 일수 계산
        result += day_2

    print(f"#{i} {result}")
