# -*- coding: utf-8 -*-  # 파일의 인코딩을 UTF-8로 설정 (한글 또는 다른 언어 사용 시 필요)

# 문자열을 뒤집는 함수 reverse 정의
def reverse(str):
    result = ""  # 결과를 저장할 빈 문자열 초기화
    for i in str:  # 입력된 문자열의 각 문자를 순서대로 탐색
        result += i  # 문자를 result에 하나씩 추가
    return result  # 완성된 문자열(사실 이 함수는 문자열을 뒤집지 않음)을 반환

# 문자열을 뒤집는 함수 reverse1 정의 (올바르게 문자열을 뒤집음)
def reverse1(str):
    return str[::-1]  # 슬라이싱 기능을 이용해 문자열을 뒤집어서 반환

# 사용자로부터 문자열 입력을 받음
str = input()

# reverse1 함수를 호출해 입력된 문자열을 뒤집음
result = reverse1(str)

# 뒤집은 결과를 출력
print(result)

# 뒤집은 문자열과 원본 문자열이 같다면 회문(Palindrome)인지 확인
if result == str:
    print("입력하신 단어는 회문(Palindrome)입니다.")  # 문자열이 회문일 경우 출력
