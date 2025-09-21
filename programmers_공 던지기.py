def solution(numbers, k):
    n = len(numbers)
    idx = 0      # 시작은 0번 인덱스 (1번 사람)
    cnt = 1      # 첫 번째 던짐은 이미 시작에서 2칸 이동한 사람

    while cnt < k:
        idx = (idx + 2) % n  # 두 칸씩 이동 (원형이므로 % n)
        cnt += 1

    return numbers[idx]


if __name__ == "__main__":
    numbers = [1, 2, 3, 4]
    k = 2
    
    numbers2 = [1, 2, 3]
    k2 = 3
    print(solution(numbers, k))  # 3
    print(solution(numbers2, k2))  # 2