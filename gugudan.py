# -*- coding: utf-8 -*-  # 인코딩 설정

gugudan = []
for i in range(2, 10):
    dan = []
    for j in range(1, 10):
        if (i * j) % 3 == 0 or (i * j) % 7 == 0:
            continue
        dan.append(i * j)
    gugudan.append(dan)
    
print(gugudan)