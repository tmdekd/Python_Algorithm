def solution(q, r, code):
    answer = ''
    
    for i in range(len(code)):
        if i % q == r:
            answer += code[i]
    return answer

if __name__ == "__main__":
    q = 3
    r = 1
    code = "qjnwezgrpirldywt"
    print(solution(q, r, code))  # "jerry"