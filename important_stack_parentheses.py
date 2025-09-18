# -*- coding: utf-8 -*-

T = int(input())

for t in range(1, T+1):
    array = input()
    result = []  # 스택 초기화
    is_valid = 1  # 기본적으로 유효하다고 가정

    for i in array:
        if i == '(' or i == '{':  # 여는 괄호 처리
            result.append(i)
        elif i == ')' or i == '}':  # 닫는 괄호 처리
            if not result:  # 스택이 비어 있으면 유효하지 않음
                is_valid = 0
                break
            last = result.pop()  # 스택에서 여는 괄호 제거
            if (i == ')' and last != '(') or (i == '}' and last != '{'):  # 짝이 맞는지 확인
                is_valid = 0
                break

    # 스택에 남은 여는 괄호가 있으면 유효하지 않음
    # 여는 괄호가 닫는 괄호보다 많은 경우
    if result:
        is_valid = 0  # 스택에 남아 있다는 것은 닫는 괄호와 짝이 맞지 않은 여는 괄호가 있다는 의미

    # 결과 출력
    print(f"#{t} {is_valid}")
