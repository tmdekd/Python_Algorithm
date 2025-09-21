def solution(s):
    answer = ''
    s = list(s)
    s.sort(reverse=True)  # 내림차순 정렬
    #  join()은 리스트의 문자열 요소들을 하나의 문자열로 합쳐주는 함수
    answer += ''.join(s)
    return answer

if __name__ == "__main__":
    s = "Zbcdefg"
    print(solution(s))  # "gfedcbZ"