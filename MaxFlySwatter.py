# -*- coding: utf-8 -*-

# 테스트 케이스의 개수를 입력받습니다.
T = int(input().strip())

# 각 테스트 케이스에 대해 반복합니다.
for t in range(1, T + 1):
    # N과 M을 입력받습니다.
    N, M = map(int, input().split())

    # N x N 배열을 입력받습니다.
    grid = []
    for _ in range(N):
        row = list(map(int, input().split()))
        grid.append(row)

    # 최대 파리 개수를 저장할 변수 초기화
    max_flies = 0

    # 모든 가능한 MxM 크기의 영역에 대해 파리의 개수를 계산합니다.
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            flies_count = 0
            # MxM 영역의 파리 개수 합을 구합니다.
            for x in range(M):
                for y in range(M):
                    flies_count += grid[i + x][j + y]
            # 최대 파리 개수 업데이트
            max_flies = max(max_flies, flies_count)

    # 결과 출력
    print(f"#{t} {max_flies}")
