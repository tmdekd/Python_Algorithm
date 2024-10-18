# -*- coding: utf-8 -*-  # 인코딩 설정

# 주어진 문자열
string = 'abcdef'

# 빈 딕셔너리 생성
dict_obj = {}

# 빈 딕셔너리의 키와 값을 변환
for i in range(len(string)):
    dict_obj[string[i]] = None  # 초기 값은 None으로 설정

# 딕셔너리 값들을 인덱스로 설정
for i in range(len(string)):
    dict_obj[string[i]] = i  # 키에 맞는 값을 인덱스로 변환

# 딕셔너리의 키와 값을 출력
for key, value in dict_obj.items():
    print(f"{key}: {value}")
