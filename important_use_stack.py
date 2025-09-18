# -*- coding: utf-8 -*-

for t in range(1, 11):  # 10개의 테스트 케이스 반복
    # 문자열 길이와 비밀번호 문자열 입력 받기
    length, string = input().split()
    length = int(length)  # 문자열 길이를 정수형으로 변환

    stack = []  # 비밀번호를 저장할 스택 초기화

    # 문자열의 각 문자를 순차적으로 스택에 처리
    # 스택을 사용한 이유는 LIFO 구조이므로 마지막에 추가도니 요소를 쉽게 확인하고
    # 제거할 수 있는 자료 구조이기 때문에
    print(stack)
    for char in string:
        # 스택이 비어있지 않고, 스택의 마지막 문자와 현재 문자가 같으면
        if (stack != []) and (stack[-1] == char):
            stack.pop()  # 같은 숫자 쌍이므로 스택에서 제거하여 소거
        else:
            stack.append(char)  # 다르면 스택에 추가

    # 최종 비밀번호 출력 (스택에 남아 있는 문자들을 이어 붙임)
    result = ""
    for i in stack:
        result += i
    print(f"#{t} {result}")
