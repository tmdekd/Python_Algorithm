# -*- coding: utf-8 -*-

# 입력받은 테스트 케이스 개수를 변수 T에 저장
T = int(input())
for i in range(1, T + 1):
    # 각 테스트 케이스마다 명령 개수 N을 입력받음
    N = int(input())
    # 총 이동 거리를 저장할 변수 distance를 초기화
    distance = 0
    # RC 카의 초기 속도를 0으로 설정
    speed = 0  # 초기 속도는 0 m/s

    # 각 명령을 반복하여 처리
    for j in range(N):
        # 각 명령을 리스트로 입력받아 command 변수에 저장
        command = list(map(int, input().split()))

        # 가속 명령(1)이 주어진 경우
        if command[0] == 1:
            # 가속도 값을 speed에 더해 현재 속도 증가
            acceleration = command[1]
            speed += acceleration
        # 감속 명령(2)이 주어진 경우
        elif command[0] == 2:
            # 감속도 값을 speed에서 빼서 속도 감소
            deceleration = command[1]
            speed -= deceleration
            # 속도가 음수가 되면 0으로 고정
            if speed < 0:
                speed = 0

        # 현재 초에서 이동한 거리(distance)를 속도(speed)만큼 증가
        distance += speed

    # 각 테스트 케이스의 결과를 형식에 맞게 출력
    print(f"#{i} {distance}")
