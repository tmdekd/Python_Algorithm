def solution(a, b):
    answer = ''
    answer = str(int(a) + int(b))
    return answer

if __name__ == "__main__":
    a = "18446744073709551615"
    b = "287346502836570928366"
    print(solution(a, b))  # "305793246910280479981"