# -*- coding: utf-8 -*-

# 테스트 케이스 수 입력
T = int(input())
# 각 테스트 케이스에 대해 반복
for test_case in range(1, T + 1):
    # 퍼즐의 크기 N과 단어의 길이 K 입력
    N, K = map(int, input().split())

    # 퍼즐 모양 입력
    puzzle = []  # 빈 리스트 생성
    for _ in range(N):
        # 한 줄을 입력받아 공백으로 나눈 후 정수로 변환하여 리스트로 만듦
        row = list(map(int, input().split()))
        # 변환된 리스트를 puzzle에 추가
        puzzle.append(row)

    # 입력된 퍼즐 모양 출력 (디버깅 용도)
    print(puzzle)

    # K 길이의 단어가 들어갈 수 있는 자리의 수를 저장할 변수
    ans = 0

    # 가로 방향 검사
    # 각 행에 대해 반복
    for row in puzzle:
        # 연속된 흰색 칸의 수를 저장하는 변수
        count = 0
        # 각 행의 각 칸에 대해 반복
        for idx, num in enumerate(row):
            # 흰색 칸이면
            if num == 1:
                # 연속된 흰색 칸 수를 1 증가
                count += 1
            # 검은색 칸을 만나면
            elif num == 0 and count != K:
                # 연속된 흰색 칸 수 초기화
                count = 0

            # 조건을 만족하는 K 길이의 단어가 들어갈 수 있는 자리인지 확인
            # 가능한 자리를 찾으면 정답에 1을 더함
            if (count == K and num == 0) or (count == K and idx == len(row) - 1):
                ans += 1
                # 연속된 흰색 칸 수 초기화
                count = 0

    # 세로 방향 검사
    # 각 열에 대해 반복
    for i in range(N):
        # 연속된 흰색 칸의 수를 저장하는 변수
        count = 0
        # 각 행의 i번째 칸에 대해 반복
        for j, row in enumerate(puzzle):
            # 흰색 칸이면
            if row[i] == 1:
                # 연속된 흰색 칸 수를 1 증가
                count += 1
            # 검은색 칸을 만나면
            elif row[i] == 0 and count != K:
                # 연속된 흰색 칸 수 초기화
                count = 0


            # 조건을 만족하는 K 길이의 단어가 들어갈 수 있는 자리인지 확인
            # 가능한 자리를 찾으면 정답에 1을 더함
            if (count == K and row[i] == 0) or (count == K and j == len(row) - 1):
                ans += 1
                # 연속된 흰색 칸 수 초기화
                count = 0

    # 각 테스트 케이스마다 결과 출력
    print(f'#{test_case} {ans}')
