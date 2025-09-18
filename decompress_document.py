# -*- coding: utf-8 -*-

# 테스트 케이스의 수를 입력받습니다.
T = int(input())

# 각 테스트 케이스를 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    document = ""  # 원본 문서를 저장할 문자열
    for _ in range(N):
        alpha, num = input().split()
        document += alpha * int(num)  # 각 알파벳과 개수를 반복하여 추가

    print(f"#{test_case}")
    # 원본 문서를 너비 10으로 출력
    for i in range(0, len(document), 10):
        print(document[i:i+10])  # 10자씩 잘라서 출력
