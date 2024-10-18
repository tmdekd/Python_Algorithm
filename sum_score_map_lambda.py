# -*- coding: utf-8 -*-  # 인코딩 설정

# 주어진 문자열
input_string = "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"

# 각 알파벳에 해당하는 점수를 딕셔너리로 정의
score_map = {'A': 4, 'B': 3, 'C': 2, 'D': 1}

# map 함수와 람다식을 사용하여 점수 계산
total_score = sum(map(lambda x: score_map[x], input_string))

print(total_score)