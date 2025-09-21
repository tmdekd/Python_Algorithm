def solution(my_str, n):
    answer = []
    for i in range(0, len(my_str), n):
        # 슬라이싱을 이용해 n개씩 잘라서 answer 리스트에 추가
        # 마지막에 남은 글자 수가 n개보다 작을 경우도 포함
        answer.append(my_str[i:i+n])
    return answer

if __name__ == "__main__":
    my_str = "abc1Ad dfggg4 556b"
    n = 6
    print(solution(my_str, n))  # ["abc1Ad", "dfggg4", "556b"]