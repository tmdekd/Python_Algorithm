# -*- coding: utf-8 -*-

# 10번 반복하는 루프 설정
for _ in range(10):
    # 입력받은 숫자를 T에 저장
    T = int(input())

    # 검색할 문자열을 입력받음
    string = input()
    # 대상 문자열을 입력받음
    search = input()
    # 대상 문자열에서 검색할 문자열의 등장 횟수를 계산
    result = search.count(string)
    # 결과를 지정된 형식으로 출력
    print(f"#{T} {result}")

