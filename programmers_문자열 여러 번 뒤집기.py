def solution(my_string, queries):
    # 문자열은 불변이라 리스트로 변환해 제자리 수정
    s_list = list(my_string)

    for s, e in queries:
        # s..e 구간을 뒤집어서 다시 할당 (제자리 갱신)
        s_list[s:e+1] = reversed(s_list[s:e+1])

    # 리스트를 다시 문자열로
    return ''.join(s_list)

if __name__ == "__main__":
    my_string = "rermgorpsam"
    queries = [[2, 3], [0, 7], [5, 9], [6, 10]]
    print(solution(my_string, queries))  # "programmers"