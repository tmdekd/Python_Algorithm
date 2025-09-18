# 단어를 거꾸로 뒤집은 결과와 원래 단어가 같은지 비교하여 회문 여부를 판단
# -*- coding: utf-8 -*-

total = int(input())
for i in range(total):
    string = input().strip()
    if string == string[::-1]:
        print(f"#{i + 1} 1")
    else:
        print(f"#{i + 1} 0")
