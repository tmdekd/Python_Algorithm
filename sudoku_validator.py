# -*- coding: utf-8 -*-

# 테스트 케이스 개수를 입력받음
T = int(input())

# 테스트 케이스마다 반복
for t in range(1, T + 1):
    # 9x9 스도쿠 퍼즐 입력받기
    array = []
    for i in range(9):
        row = list(map(int, input().split()))
        array.append(row)

    # 스도쿠 검증 변수
    is_valid = True

    # 행과 열 검사
    for i in range(9):
        row_set = set()
        col_set = set()

        for j in range(9):
            # 행 검사
            if array[i][j] in row_set:
                is_valid = False
                break
            row_set.add(array[i][j])

            # 열 검사
            if array[j][i] in col_set:
                is_valid = False
                break
            col_set.add(array[j][i])

        if not is_valid:
            break

    # 3x3 영역 검사
    if is_valid:
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                square_set = set()
                for x in range(3):
                    for y in range(3):
                        num = array[i + x][j + y]
                        if num in square_set:
                            is_valid = False
                            break
                        square_set.add(num)
                if not is_valid:
                    break
            if not is_valid:
                break

    # 스도쿠 검증 결과 출력
    if is_valid:
        result = 1
    else:
        result = 0
    print(f"#{t} {result}")

