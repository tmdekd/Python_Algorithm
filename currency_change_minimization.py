# -*- coding: utf-8 -*-

T = int(input())  # 테스트 케이스의 개수 입력
for t in range(1, T + 1):  # 테스트 케이스 번호는 1부터 시작
    N = int(input())  # 거슬러 줄 금액 입력
    # 각 화폐 단위를 리스트로 정의
    money_units = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    count_list = []  # 각 화폐의 개수를 저장할 리스트

    for unit in money_units:
        count = N // unit  # 해당 화폐 단위로 나눈 몫이 필요 개수
        count_list.append(count)  # 개수를 리스트에 추가
        N %= unit  # 나머지를 계산하여 다음 단위에 대해 계산

    # 출력 형식에 맞게 출력
    print(f"#{t}")
    print(*count_list)

