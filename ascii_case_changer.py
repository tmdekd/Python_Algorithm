# -*- coding: utf-8 -*-
# 문제:
# 입력된 문자가 대문자일 경우 소문자로, 소문자일 경우 대문자로 변경하고,
# 알파벳이 아닐 경우엔 그냥 출력하는 코드를 작성하십시오.
# 출력 시 아스키 코드를 함께 출력합니다.
#
# [입력 예시]
# c
# ex_025_input.txt
#
# [출력 예시]
# c(ASCII: 99) => C(ASCII: 67)

# 입력받은 문자를 char 변수에 저장
char = input()

# 입력된 문자가 소문자일 경우 대문자로, 대문자일 경우 소문자로 변환하여 출력
# 아스키 코드 값을 함께 출력
if char.islower():  # 소문자인 경우
    print(f"{char}(ASCII: {ord(char)}) => {chr(ord(char)-32)}(ASCII: {ord(char)-32})")
elif char.isupper():  # 대문자인 경우
    print(f"{char}(ASCII: {ord(char)}) => {chr(ord(char)+32)}(ASCII: {ord(char)+32})")
else:
    # 알파벳이 아닐 경우는 그대로 출력
    print(f"{char}(ASCII: {ord(char)}) => {char}(ASCII: {ord(char)})")
