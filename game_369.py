# -*- coding: utf-8 -*-

N = int(input())

for n in range(1, N + 1):
    # 숫자를 문자열로 변환하여 "3", "6", "9"의 개수를 센다
    count_3 = str(n).count('3')
    count_6 = str(n).count('6')
    count_9 = str(n).count('9')

    # 총 박수 횟수는 "3", "6", "9"의 개수를 더한 값
    clap_count = count_3 + count_6 + count_9

    if clap_count > 0:
        # 박수 횟수에 맞게 "-"를 출력
        print("-" * clap_count, end=" ")
    else:
        # 3, 6, 9가 포함되지 않은 경우 숫자를 그대로 출력
        print(n, end=" ")
