# -*- coding: utf-8 -*-

# 테스트 케이스 개수를 입력받음
T = int(input())
for t in range(1, T + 1):
    # 각 테스트 케이스의 행렬 크기 N을 입력받음
    N = int(input())
    array = []

    # 행렬 입력 받기 (N x N 크기의 2차원 배열 생성)
    for _ in range(N):
        # 각 행의 숫자를 공백으로 구분하여 입력받아 리스트로 저장
        row = list(map(int, input().split()))
        array.append(row)  # 입력받은 행을 행렬(array)에 추가

    # 회전 결과 저장을 위한 90도, 180도, 270도 회전 행렬 초기화 (N x N 크기)
    rotate_90 = [[0] * N for _ in range(N)]
    rotate_180 = [[0] * N for _ in range(N)]
    rotate_270 = [[0] * N for _ in range(N)]

    # 90도, 180도, 270도 회전 결과 계산
    for i in range(N):
        for j in range(N):
            # 90도 회전: 원래 (i, j) 위치의 요소를 (j, N - 1 - i) 위치로 이동
            rotate_90[j][N - 1 - i] = array[i][j]
            # 180도 회전: 원래 (i, j) 위치의 요소를 (N - 1 - i, N - 1 - j) 위치로 이동
            rotate_180[N - 1 - i][N - 1 - j] = array[i][j]
            # 270도 회전: 원래 (i, j) 위치의 요소를 (N - 1 - j, i) 위치로 이동
            rotate_270[N - 1 - j][i] = array[i][j]

    # 각 테스트 케이스 번호 출력
    print(f"#{t}")
    # 출력 형식에 맞춰 회전된 행렬 출력
    # i번째 행을 하나씩 가져와서 문자열로 변환하고 공백으로 구분된 출력문을 생성
    for i in range(N):
        # 90도 회전된 i번째 행을 문자열로 변환
        row_90 = ""
        for num in rotate_90[i]:
            row_90 += str(num)

        # 180도 회전된 i번째 행을 문자열로 변환
        row_180 = ""
        for num in rotate_180[i]:
            row_180 += str(num)

        # 270도 회전된 i번째 행을 문자열로 변환
        row_270 = ""
        for num in rotate_270[i]:
            row_270 += str(num)

        # 각 행을 공백으로 구분하여 출력
        print(row_90 + " " + row_180 + " " + row_270)
