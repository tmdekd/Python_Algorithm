# -*- coding: utf-8 -*-

# 각 혈액형 별로 카운트를 초기화
count_a = 0
count_b = 0
count_o = 0
count_ab = 0

# 학생들의 혈액형 데이터
data = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']

# for 문을 이용하여 각 혈액형 별로 카운트를 증가시킴
for i in data:
    if i == 'A':
        count_a += 1
    elif i == 'B':
        count_b += 1
    elif i == 'O':
        count_o += 1
    elif i == 'AB':
        count_ab += 1

# f-string을 사용하여 결과를 딕셔너리 형태로 출력
# 중괄호 자체를 출력하고 싶을 때는 f-string이 이를 포맷팅 문법으로 인식하지 않도록 이중 중괄호 {{와 }}를 사용해야 합니다.
print(f"{{'A': {count_a}, 'O': {count_o}, 'B': {count_b}, 'AB': {count_ab}}}")
