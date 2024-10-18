# 리스트 list_a 생성: 1부터 10까지의 정수를 포함
list_a = list(range(1, 11))

# filter()로 list_a에서 짝수만 필터링하고, map()으로 필터링된 짝수들의 제곱을 계산
# filter(lambda y : y % 2 == 0, list_a): list_a에서 짝수만 남김
# map(lambda x : x ** 2, ...): 짝수들의 제곱 값을 계산
# 최종적으로 짝수의 제곱 리스트를 출력
result = list(map(lambda x : x ** 2, list(filter(lambda y : y % 2 == 0, list_a))))

print(result)  # [4, 16, 36, 64, 100]
