def solution(arr):
    count = 0
    while True:
        new_arr = []
        for v in arr:
            if v >= 50 and v % 2 == 0:
                new_arr.append(v // 2)
            elif v < 50 and v % 2 == 1:
                new_arr.append(v * 2 + 1)
            else:
                new_arr.append(v)

        # arr : 기존 배열, new_arr : 변화된 배열
        if new_arr == arr:      # 더 이상 변화가 없으면 종료
            return count
        arr = new_arr
        count += 1

if __name__ == "__main__":
    arr = [1, 2, 3, 100, 99, 98]
    print(solution(arr))  # 5