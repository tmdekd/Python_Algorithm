# 리스트 정의
fruits = ['apple', 'banana', 'cherry']

# enumerate 함수 사용, 기본 인덱스는 0부터 시작
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")

print("=========================")

# enumerate 함수 사용, 인덱스는 1부터 시작
for index, fruit in enumerate(fruits, start=1):
    print(f"Index: {index}, Fruit: {fruit}")