# -*- coding: utf-8 -*-  # 파일의 인코딩을 UTF-8로 설정 (한글 또는 다른 언어 사용 시 필요)

# 사용자로부터 10진수를 입력받아, 파이썬 내장 함수로 2진수로 변환하는 코드
decimal_number = int(input())  # 사용자로부터 정수를 입력받음
binary_number = bin(decimal_number)[2:]  # bin() 함수로 2진수 변환 후, 앞의 '0b' 제거
print(binary_number)  # 변환된 2진수 출력

print("=====")  # 구분선 출력

# 직접 10진수를 2진수로 변환하는 함수 정의
def decimal_to_binary(n):
    binary_num = ''  # 2진수 값을 저장할 문자열 초기화
    
    if n == 0:  # 입력이 0인 경우 바로 '0' 반환
        return '0'
    
    # n이 0이 될 때까지 2로 나누며 나머지를 구하는 반복문
    while n > 0:
        remainder = n % 2  # n을 2로 나눈 나머지(현재 자리의 이진수 값) 구함
        binary_num = str(remainder) + binary_num  # 나머지를 문자열로 변환해 앞에 붙임
        n = n // 2  # n을 2로 나눈 몫을 다시 n에 할당 (반복 진행)
    
    return binary_num  # 완성된 2진수 문자열 반환

# 사용자로부터 10진수를 입력받아, 위에서 정의한 함수로 2진수로 변환하는 코드
decimal_number = int(input())  # 사용자로부터 정수를 입력받음
binary_number = decimal_to_binary(decimal_number)  # 직접 구현한 변환 함수 호출
print(binary_number)  # 변환된 2진수 출력
