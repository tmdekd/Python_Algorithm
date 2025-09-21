def solution(arr1, arr2):
    n = len(arr1)
    m = len(arr1[0])
    answer = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            sum_value = arr1[i][j] + arr2[i][j]
            answer[i][j] = sum_value
    return answer

if __name__ == "__main__":
    arr1 = [[1, 2], [2, 3]]
    arr2 = [[3, 4], [5, 6]]
    print(solution(arr1, arr2))  # Expected output: [[4, 6], [7, 9]]