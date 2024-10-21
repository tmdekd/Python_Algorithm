# -*- coding: utf-8 -*-  # 인코딩 설정

# 원본 문자열
string = 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'
# 소문자 모음들
char = 'aeiou'

# 리스트 내포를 사용하여 소문자 모음이 아닌 문자들만 모아서 새로운 문자열을 만듦
# 각 문자를 순차적으로 검사하여, 소문자 모음('aeiou')이 아닐 경우만 새로운 문자열에 추가함
result = ''.join([i for i in string if i not in char])

# 결과 출력: 소문자 모음이 제거된 문자열이 출력됨
print(result)
