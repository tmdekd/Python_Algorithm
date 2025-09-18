# -*- coding: utf-8 -*-

T = int(input())  # 테스트 케이스 수 입력
for t in range(1, T + 1):
    N = int(input())  # 칠할 영역의 개수 입력
    grid = []
    for _ in range(10):
        grid.append([0]*10)

    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                grid[i][j] += color  # 색깔 정보 누적

        # 보라색(빨강+파랑=3)인 칸 수 계산
        # 색을 칠한 영역 안에서 보라색인 칸 수를 계산하면 되기에
        # 전체 탐색을 할 필요가 없음
        purple_count = 0
        for i in range(10):
            for j in range(10):
                if grid[i][j] == 3:
                    purple_count += 1

    print(f"#{t} {purple_count}")
