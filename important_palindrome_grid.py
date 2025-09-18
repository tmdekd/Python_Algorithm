# -*- coding: utf-8 -*-

# 테스트 케이스 개수 입력받음
T = int(input())
for t in range(1, T + 1):
    # n: 배열 크기, m: 찾고자 하는 회문의 길이
    n, m = map(int, input().split())
    array = []
    for _ in range(n):
        array.append(input())

    result = ""

    # 가로 방향 회문 검색
    for row in range(n):
        for start in range(n - m + 1):
            substring = array[row][start:start + m]  # 가로 방향 부분 문자열
            if substring == substring[::-1]:  # 회문인지 확인
                result = substring
                break
        if result:  # 회문을 찾으면 종료
            break

    # 세로 방향 회문 검색
    if not result:  # 가로에서 회문을 찾지 못한 경우에만 실행
        for col in range(n):
            for start in range(n - m + 1):
                substring = ""  # 세로 방향 부분 문자열 초기화

                # 특정 열(col)에서 시작 위치(start)로부터 연속된 m개의 문자를 가져옵니다.
                for i in range(m):
                    substring += array[start + i][col]  # 세로 방향 문자열 구성

                if substring == substring[::-1]:  # 회문인지 확인
                    result = substring
                    break
            if result:  # 회문을 찾으면 종료
                break

    # 결과 출력 (테스트 케이스 번호와 회문 문자열)
    print(f"#{t} {result}")
