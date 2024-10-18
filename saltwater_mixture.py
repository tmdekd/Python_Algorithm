# -*- coding: utf-8 -*-
# 문제
# 20% 농도의 소금물 100g과 물 200g을 혼합한 소금물의 농도(%)를 소수점 두 번째 자리까지 구하는 프로그램을 작성하십시오.

# 출력
# 혼합된 소금물의 농도: 6.67%

# 문제풀이
# 20% 농도의 소금물 100g에는 소금이 얼마 있는지 계산합니다.
# 20% 농도란, 100g 중 20g이 소금이고 나머지 80g이 물임을 의미합니다.
# 물 200g은 순수한 물이므로 소금이 없습니다.
# 두 용액(소금물과 물)을 섞었을 때, 혼합된 소금물의 농도를 구하려면 전체 소금의 양을 전체 용액의 양으로 나누고, 이를 백분율로 표현해야 합니다.

# 20% 농도의 소금물 100g과 물 200g을 혼합한 소금물의 농도 구하기

saltwater_concentration = 20  # 20%
saltwater_amount = 100        # 100g 소금물
water_amount = 200            # 200g 물

# 1. 소금의 양을 계산 (소금물의 농도에 따른 소금의 양)
salt_amount = (saltwater_concentration / 100) * saltwater_amount

# 2. 전체 혼합 용액의 양
total_solution_amount = saltwater_amount + water_amount

# 3. 혼합 소금물의 농도를 계산
new_concentration = (salt_amount / total_solution_amount) * 100

# 결과 출력
print(f"혼합된 소금물의 농도: {new_concentration:.2f}%")
