def solution(my_string):
    answer = 0
    tokens = my_string.split()  # 공백 기준 분리 → ["3", "+", "4"]

    # 첫 숫자를 초기값으로 설정
    answer = int(tokens[0])
    op = "+"  # 기본 연산자는 더하기

    # 두 번째 토큰부터 순회
    for token in tokens[1:]:
        if token in ["+", "-"]:  # 연산자면 op에 저장
            op = token
        else:  # 숫자라면, 직전 연산자에 따라 처리
            num = int(token)
            if op == "+":
                answer += num
            elif op == "-":
                answer -= num

    return answer

if __name__ == "__main__":
    my_string = "3 + 4"
    print(solution(my_string))  # 7