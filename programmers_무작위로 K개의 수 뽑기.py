def solution(arr, k):
    answer = []
    seen = set()   # 이미 나온 숫자를 기억하는 집합

    for num in arr:
        if num not in seen:   # 처음 나온 숫자라면
            answer.append(num)
            seen.add(num)

        if len(answer) == k:  # k개를 다 모으면 끝
            break

    # k개가 안 채워졌으면 나머지를 -1로 채움
    while len(answer) < k:
        answer.append(-1)

    return answer

if __name__ == "__main__":
    arr = [0, 1, 1, 2, 2, 3]	
    k = 3
    print(solution(arr, k))  # Expected output: [0, 1, 2]