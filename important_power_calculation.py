# -*- coding: utf-8 -*-

# 재귀 함수를 이용하여 N의 M 거듭제곱 값을 계산하는 함수
def power(N, M):
    # 기저 조건: M이 1일 때는 N을 그대로 반환
    if M == 1:
        return N
    # 재귀 호출: N * power(N, M-1)을 반환하여 N을 M번 곱하는 구조
    return N * power(N, M - 1)

# 10번 반복하는 루프 설정 (테스트 케이스가 10개 주어짐)
for _ in range(10):
    # 테스트 케이스 번호를 입력받음
    T = int(input())
    # N과 M을 입력받음
    N, M = map(int, input().split())
    # N의 M 거듭제곱 값을 계산
    result = power(N, M)
    # 결과 출력
    print(f"#{T} {result}")
