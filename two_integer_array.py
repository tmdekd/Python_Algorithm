# 두 개의 숫자열을 주어진 범위 내에서 서로 맞춰 곱셈한 결과의 합 중 최댓값을 구하는 문제입니다.
# 숫자열 중 더 긴 쪽을 기준으로 이동하며 최댓값을 찾습니다.

# -*- coding: utf-8 -*-

# 테스트 케이스의 수를 입력받음
T = int(input())
for t in range(1, T + 1):
    # N과 M을 입력받음
    N, M = map(int, input().split())

    # 숫자열 A와 B를 입력받음
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # A와 B 중 더 긴 숫자열을 B로 설정하여 일관되게 처리
    if N > M:
        A, B = B, A
        N, M = M, N

    # A를 B 안에서 이동하며 첫 번째 곱셈 합을 계산하여 max_sum 초기화
    # j번째끼리 곱하는 것은 현재 위치에서 서로 대응되는 두 숫자열의 요소를 곱해 합산하여 max_sum을 초기화하기 위함.
    max_sum = sum(A[j] * B[j] for j in range(N))

    # 두 번째 위치부터 마지막 위치까지 계산하여 최댓값 찾기
    for i in range(1, M - N + 1):
        current_sum = sum(A[j] * B[i + j] for j in range(N))
        max_sum = max(max_sum, current_sum)

    # 결과 출력
    print(f"#{t} {max_sum}")
