def solution(arr, queries):
    for s, e, k in queries:
        # s부터 e까지 차례대로 확인
        for i in range(s, e + 1):
            # i가 k의 배수라면 arr[i]에 +1
            if k != 0 and i % k == 0:
                arr[i] += 1
            # k=0일 경우, 0의 배수는 0뿐이므로 따로 처리
            elif k == 0 and i == 0:
                arr[0] += 1
    return arr

if __name__ == "__main__":
    arr = [0, 1, 2, 4, 3]
    queries = [[0, 4, 1],[0, 3, 2],[0, 3, 3]]
    print(solution(arr, queries))  # [3, 2, 4, 6, 4]
