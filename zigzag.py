# -*- coding: utf-8 -*-  # UTF-8 인코딩을 사용하여 소스 코드 작성

# 사용자로부터 정수 n을 입력받습니다.
n = int(input())

# 1부터 n까지 반복합니다.
for i in range(1, n+1):
    # 각 테스트 케이스에 대해 정수 num을 입력받습니다.
    num = int(input())
    sum = 0  # 합계를 저장할 변수를 초기화합니다.
    
    # 1부터 num까지 반복합니다.
    for j in range(1, num+1):
        if j == 1:
            sum += j  # j가 1이면 sum에 1을 더합니다.
        else:
            if j % 2 == 0:
                sum -= j  # j가 짝수이면 sum에서 j를 뺍니다.
            elif j % 2 != 0:
                sum += j  # j가 홀수이면 sum에 j를 더합니다.
    
    # 각 테스트 케이스의 결과를 출력합니다. 형식은 "#i sum"입니다.
    print(f"#{i} {sum}")
