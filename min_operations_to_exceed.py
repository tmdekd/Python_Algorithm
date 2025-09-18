# -*- coding: utf-8 -*-

T = int(input())  # 테스트 케이스의 개수 입력
for t in range(T):
    x, y, n = map(int, input().split())
    result = 0

    while x <= n and y <= n:
        # 작은 값에 큰 값을 더하는 것이 더 빠르기 때문
        if x < y:
            x += y  # x가 y보다 작으면 x에 y를 더함
        else:
            y += x  # y가 x보다 작거나 같으면 y에 x를 더함
        result += 1  # 연산 횟수 증가

    print(result)
