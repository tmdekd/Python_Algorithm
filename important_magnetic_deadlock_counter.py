# -*- coding: utf-8 -*-

# 10개의 테스트 케이스 처리
for t in range(1, 11):
    size = int(input())  # 항상 100으로 고정됨

    table = []
    # 100x100 테이블 입력
    for _ in range(size):
        row = list(map(int, input().split()))
        table.append(row)

    count = 0  # 교착 상태 개수

    # 각 열을 위에서 아래로 탐색하여 교착 상태를 세기
    # 교착 상태의 경우, 위에서 아래로 탐색하면 N극 자성체(1)가 먼저 등장하고 S극 자성체(2)가 뒤따라서 등장하는 구조가 만들어진다.
    # 이 순서가 있어야 교착 상태를 올바르게 세울 수 있습니다.
    for col in range(size):
        previous = 0  # 이전 자성체 상태 (0으로 초기화)

        for row in range(size):
            if table[row][col] == 1:  # N극 자성체 발견
                previous = 1  # 다음에 S극 자성체(2)를 만나면 교착 상태로 인식

            elif table[row][col] == 2:  # S극 자성체 발견
                if previous == 1:  # 이전에 N극 자성체가 있었던 경우
                    count += 1  # N극과 S극 자성체가 만나 교착 상태 발생

                # 다음 교착 상태를 위해 previous를 0으로 초기화
                # 이유: 현재 교착 상태를 이미 카운트했기 때문에 이전 N극 자성체와는 더 이상 상관이 없고,
                # 새로운 교착 상태를 기다리는 상태로 돌아가야 함.
                # 예를 들어, S극 자성체(2)가 연속으로 나타날 경우 중복 카운트를 방지하고,
                # 다음 N극 자성체(1)가 등장할 때 새로운 교착 상태로 시작하도록 한다.
                # 초기화하지 않으면, 여전히 previous는 1이므로 count가 하나 더 증가하게 된다. 그래서 previous 초기화 필요
                previous = 0

    # 결과 출력
    print(f"#{t} {count}")
