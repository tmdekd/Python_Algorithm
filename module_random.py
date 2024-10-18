# -*- coding: utf-8 -*-  # 인코딩 설정

import random  # random 모듈을 불러옵니다.

# 1. random.random()
# 0.0에서 1.0 사이의 임의의 부동소수점(float) 값을 반환합니다.
random_float = random.random()
print(f"1. random.random(): {random_float}")

# 2. random.randint(a, b)
# a에서 b 사이의 임의의 정수(int)를 반환합니다. (a와 b 모두 포함)
random_int = random.randint(1, 10)
print(f"2. random.randint(1, 10): {random_int}")

# 3. random.uniform(a, b)
# a에서 b 사이의 임의의 부동소수점 값을 반환합니다. (a와 b 모두 포함)
random_uniform = random.uniform(1.5, 10.5)
print(f"3. random.uniform(1.5, 10.5): {random_uniform}")

# 4. random.choice(sequence)
# 주어진 시퀀스(리스트, 문자열, 튜플 등)에서 임의의 항목을 반환합니다.
fruits = ['apple', 'banana', 'cherry', 'date']
random_choice = random.choice(fruits)
print(f"4. random.choice(fruits): {random_choice}")

# 5. random.choices(sequence, k=N)
# 주어진 시퀀스에서 중복을 허용하여 N개의 항목을 임의로 선택합니다.
# 예를 들어, fruits 리스트에서 중복을 허용하여 3개를 선택
random_choices = random.choices(fruits, k=3)
print(f"5. random.choices(fruits, k=3): {random_choices}")

# 6. random.sample(sequence, k=N)
# 주어진 시퀀스에서 중복 없이 N개의 항목을 임의로 선택합니다.
# 예를 들어, fruits 리스트에서 중복 없이 2개를 선택
random_sample = random.sample(fruits, k=2)
print(f"6. random.sample(fruits, k=2): {random_sample}")

# 7. random.shuffle(sequence)
# 주어진 시퀀스의 항목을 임의로 섞습니다. 원본 시퀀스를 수정합니다.
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(f"7. random.shuffle(numbers): {numbers}")

# 8. random.randrange(start, stop[, step])
# start에서 stop 사이에서 step 간격의 임의의 정수를 반환합니다. (stop은 포함되지 않음)
random_range = random.randrange(0, 100, 10)
print(f"8. random.randrange(0, 100, 10): {random_range}")
