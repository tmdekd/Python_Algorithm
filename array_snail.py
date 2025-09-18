# -*- coding: utf-8 -*-

# 테스트 케이스 개수를 입력받음
T = int(input())
for t in range(1, T + 1):
    # 달팽이 배열 크기 N을 입력받음
    N = int(input())

    # N x N 크기의 2차원 배열 초기화 (모든 요소를 0으로 설정)
    snail = [[0] * N for _ in range(N)]

    # 초기값 설정
    num = 1  # 채워 넣을 숫자 (1부터 시작)
    i, j = 0, 0  # 시작 위치
    direction = 'right'  # 첫 번째 방향은 오른쪽으로 시작

    # N x N 배열을 채울 때까지 반복
    while num <= N * N:
        # 현재 위치에 숫자 배치
        snail[i][j] = num
        num += 1

        # 다음 위치 계산
        if direction == 'right':
            # 오른쪽으로 이동 가능 조건:
            # 1. 현재 열 `j`가 N-1보다 작아야 함 (오른쪽 경계 안쪽에 위치).
            # 2. 다음 위치 `snail[i][j + 1]`가 0이어야 함 (아직 숫자가 채워지지 않은 자리).
            if j < N - 1 and snail[i][j + 1] == 0:
                j += 1  # 오른쪽으로 한 칸 이동
            else:  # 끝에 도달하면 아래로 꺾기
                direction = 'down'
                i += 1  # 방향을 아래로 바꾸고 행을 증가

        elif direction == 'down':
            # 아래로 이동 가능 조건:
            # 1. 현재 행 `i`가 N-1보다 작아야 함 (아래쪽 경계 안쪽에 위치).
            # 2. 다음 위치 `snail[i + 1][j]`가 0이어야 함 (아직 숫자가 채워지지 않은 자리).
            if i < N - 1 and snail[i + 1][j] == 0:
                i += 1  # 아래로 한 칸 이동
            else:  # 끝에 도달하면 왼쪽으로 꺾기
                direction = 'left'
                j -= 1  # 방향을 왼쪽으로 바꾸고 열을 감소

        elif direction == 'left':
            # 왼쪽으로 이동 가능 조건:
            # 1. 현재 열 `j`가 0보다 커야 함 (왼쪽 경계 안쪽에 위치).
            # 2. 다음 위치 `snail[i][j - 1]`가 0이어야 함 (아직 숫자가 채워지지 않은 자리).
            if j > 0 and snail[i][j - 1] == 0:
                j -= 1  # 왼쪽으로 한 칸 이동
            else:  # 끝에 도달하면 위로 꺾기
                direction = 'up'
                i -= 1  # 방향을 위로 바꾸고 행을 감소

        elif direction == 'up':
            # 위로 이동 가능 조건:
            # 1. 현재 행 `i`가 0보다 커야 함 (위쪽 경계 안쪽에 위치).
            # 2. 다음 위치 `snail[i - 1][j]`가 0이어야 함 (아직 숫자가 채워지지 않은 자리).
            if i > 0 and snail[i - 1][j] == 0:
                i -= 1  # 위로 한 칸 이동
            else:  # 끝에 도달하면 오른쪽으로 꺾기
                direction = 'right'
                j += 1  # 방향을 오른쪽으로 바꾸고 열을 증가

    # 결과 출력
    print(f"#{t}")

    # 각 행의 각 숫자를 공백으로 구분하여 출력
    for row in snail:
        row_output = ""
        for num in row:
            row_output += str(num) + " "  # 각 숫자를 문자열로 변환 후 공백 추가
        print(row_output.strip())  # 줄 끝 공백 제거 후 출력 / strip()을 통해 앞 뒤 공백 제거 가능, 중간 공백은 제거 X
