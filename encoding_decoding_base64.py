# Base64 인코딩 문자열을 디코딩하여 원문을 복원하는 문제.

# -*- coding: utf-8 -*-
# 테스트 케이스 수 입력
T = int(input())

# 각 테스트 케이스 처리
for t in range(1, T + 1):
    # Base64로 인코딩된 문자열 입력
    code = input().strip()
    
    # Base64 문자 집합 정의
    # Base64 인코딩 표에 있는 64개의 문자들을 문자열로 정의합니다.
    # 각 문자의 인덱스가 Base64에서의 숫자 값과 동일합니다.
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    
    # 이진수 문자열을 저장할 변수 초기화
    binary_string = ""
    
    # 입력된 Base64 문자열을 이진수 문자열로 변환
    for char in code:
        # 각 Base64 문자의 인덱스를 찾고, 6비트 이진수로 변환한 후, 이진수 문자열에 추가
        # `:06b` 포맷을 사용하여 6비트 이진수로 고정 길이 문자열을 만듭니다.
        binary_string += f"{base64_chars.index(char):06b}"
        print(f"{char} -> {base64_chars.index(char):06b}")
    
    # 디코딩된 텍스트를 저장할 변수 초기화
    decoded_text = ""
    
    # 이진수 문자열을 8비트씩 나누어 ASCII 문자로 변환
    for i in range(0, len(binary_string), 8):
        # 8비트씩 잘라서 한 바이트로 처리
        byte = binary_string[i:i+8]
        print(f"i : {i}일 때 byte: {byte}")
        # 바이트가 8비트가 아니면 패딩으로 인해 남는 부분이므로 무시합니다.
        if len(byte) == 8:
            # 8비트 이진수를 정수로 변환하고, 해당 정수를 ASCII 문자로 변환하여 결과에 추가
            decoded_text += chr(int(byte, 2))
            print(f"{i}일때, {decoded_text}")
    
    # 출력 형식에 맞춰 결과 출력
    print(f"#{t}", decoded_text)
