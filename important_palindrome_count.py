# -*- coding: utf-8 -*-

# 총 10개의 테스트 케이스 처리
for t in range(1, 11):
    # 회문의 길이를 입력받음
    length = int(input())
    # 8x8 크기의 글자 배열을 입력받음
    array = []
    for _ in range(8):
        row = input()  # 한 줄의 문자열을 입력받음
        array.append(row)  # 배열에 추가

    count = 0  # 회문의 개수를 저장할 변수 초기화

    # 가로 방향으로 회문 검색
    for row in range(8):  # 각 행을 순회
        # 한 행 내에서 가능한 모든 시작 지점 설정
        # (전체 길이 8 - 회문 길이 length + 1)을 해야 0부터 가능한 마지막 시작 지점까지 커버됨
        for start in range(8 - length + 1):
            # 회문 길이만큼 부분 문자열을 추출
            substring = array[row][start:start + length]
            # 추출한 부분 문자열이 회문인지 확인
            if substring == substring[::-1]:  # 문자열을 뒤집어 비교
                count += 1  # 회문일 경우 count 증가

    # 세로 방향으로 회문 검색
    for col in range(8):  # 각 열을 순회
        # 한 열 내에서 가능한 모든 시작 지점 설정
        for start in range(8 - length + 1):
            # 세로 방향으로 문자열을 하나씩 추가하여 회문 길이만큼의 문자열을 만듦
            substring = ""  # 세로 방향 문자열 초기화
            for i in range(length):
                # 세로 방향으로 특정 열(col)의 행(start + i)에서 문자를 가져와 추가
                substring += array[start + i][col]

            # 추출한 세로 방향 문자열이 회문인지 확인
            if substring == substring[::-1]:  # 문자열을 뒤집어 비교
                count += 1  # 회문일 경우 count 증가

    # 결과 출력 (테스트 케이스 번호와 회문 개수)
    print(f"#{t} {count}")
