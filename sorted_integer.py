# -*- coding: utf-8 -*-

# 테스트 케이스 개수를 입력 받음
T = int(input())

# 각 테스트 케이스에 대해 반복
for t in range(1, T + 1):
    # N을 입력받음
    N = int(input())

    # N개의 숫자를 입력받아 리스트로 변환
    num_list = list(map(int, input().split()))

    # 리스트를 오름차순으로 정렬
    num_list.sort()

    # 결과 출력
    print(f"#{t}", *num_list)  # '*'를 사용하여 리스트를 공백으로 구분하여 출력
