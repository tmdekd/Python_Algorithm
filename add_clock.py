# -*- coding: utf-8 -*-

T = int(input())
for t in range(T):
    hour_1, minute_1, hour_2, minute_2 = map(int, input().split())
    hour = hour_1 + hour_2
    minute = minute_1 + minute_2

    if hour >= 13:
        hour -= 12
    if minute >= 60:
        hour += 1
        minute -= 60



    print(f"#{t+1} {hour} {minute}")