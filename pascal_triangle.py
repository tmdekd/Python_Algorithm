# -*- coding: utf-8 -*-

# 테스트 케이스 개수를 입력받음
T = int(input())

# 테스트 케이스마다 반복
for t in range(1, T + 1):
    N = int(input())

    # 파스칼의 삼각형을 저장할 리스트 초기화
    pascal_triangle = []
    for i in range(N):
        row = [1] * (i + 1)
        pascal_triangle.append(row)

    # 파스칼의 삼각형 계산
    # 세 번째 줄부터 값이 1이 아닌 요소가 존재하기 때문에
    for i in range(2, N):
        # 각 줄의 첫 번째와 마지막 요소는 항상 1이므로 범위가 1부터 i-1까지 이다.
        for j in range(1, i):
            pascal_triangle[i][j] = pascal_triangle[i - 1][j - 1] + pascal_triangle[i - 1][j]

    # 출력
    print(f"#{t}")
    for row in pascal_triangle:
        # print(*row)는 리스트 row의 모든 요소를 공백으로 구분하여 출력합니다.
        print(*row)
