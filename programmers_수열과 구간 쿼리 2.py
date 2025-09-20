def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        # 후보 값을 담을 리스트
        print('s, e, k:', s, e, k)
        tmp = []

        # s부터 e까지 arr를 순회
        for i in range(s, e + 1):
            value = arr[i]

            # 조건: k보다 큰 값만 후보에 추가
            if value > k:
                tmp.append(value)

        # 후보가 비어 있으면 -1, 있으면 최솟값을 결과에 추가
        if len(tmp) == 0:
            answer.append(-1)
        else:
            min_value = min(tmp)
            answer.append(min_value)

    return answer

if __name__ == "__main__":
    arr = [0, 1, 2, 4, 3]
    queries = [[0, 4, 2],[0, 3, 2],[0, 2, 2]]
    print(solution(arr, queries))  # 출력: [3, 4, -1]