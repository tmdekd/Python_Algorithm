# -*- coding: utf-8 -*-  # 인코딩 설정

# 소수를 구분하는 함수 정의
def test(num):
    result = True  # 일단 True로 설정 (소수라고 가정)
    
    if num <= 1:  # 1 이하의 숫자는 소수가 아님
        result = False
    else:
        # 2부터 num-1까지 반복하면서 나누어 떨어지는지 확인
        for i in range(2, num):  # √num까지만 확인하는 것이 더 효율적
            if num % i == 0:  # num이 i로 나누어 떨어지면 소수가 아님
                result = False
                break  # 한 번이라도 나누어 떨어지면 반복을 멈춤
    
    # 결과에 따라 소수인지 아닌지 출력
    if result == True:
        print("소수입니다.")
    else:
        print("소수가 아닙니다.")

# 사용자로부터 입력받은 숫자가 소수인지 확인
num = int(input())
test(num)
