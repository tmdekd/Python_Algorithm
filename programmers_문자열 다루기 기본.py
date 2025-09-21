def solution(s):
    answer = True

    if (len(s) == 4 or len(s) == 6) and s.isdigit() == True:
        answer = True
    else:
        answer = False
    return answer

if __name__ == "__main__":
    s = "a234"
    print(solution(s))  # Expected output: false