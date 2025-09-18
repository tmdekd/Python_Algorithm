# -*- coding: utf-8 -*-

# 10개의 테스트 케이스
for t in range(1, 11):
    # 건물 개수 입력
    n = int(input())
    # 건물 높이 리스트 입력
    heights = list(map(int, input().split()))

    # 조망권 확보된 세대 수
    view_count = 0

    # 인덱스 2부터 n-3까지 검사 (양쪽 두 칸을 제외)
    for i in range(2, n - 2):
        # 현재 빌딩의 양옆 두 칸 중 최대 높이.
        # 현재 빌딩의 양옆 두 칸 중 최대 높이가 현재 빌딩보다 낮기만 하면 조망권이 한 세대 이상 확보되기 때문
        max_adjacent_height = max(heights[i-2], heights[i-1], heights[i+1], heights[i+2])

        # 현재 빌딩이 양옆 두 칸보다 높은 경우
        if heights[i] > max_adjacent_height:
            # 조망권이 확보된 세대 수를 계산하여 누적
            view_count += heights[i] - max_adjacent_height

    # 결과 출력
    print(f"#{t} {view_count}")
