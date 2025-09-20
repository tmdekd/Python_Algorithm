def solution(arr, idx):
    answer = 0
    # idx부터 arr의 끝까지 순회
    for i in range(idx, len(arr)):
        # 만약 원소가 1이면 해당 인덱스를 반환
        if arr[i] == 1:
            answer = i
            break
        # 1을 못 찾으면 answer를 -1로 유지
        answer = -1
    return answer

def solution2(arr, idx):
    answer = 0
    try:
        # arr.index(x, start)는 arr[start:]에서 x의 위치를 찾음
        # idx부터 탐색해 처음 나오는 1의 인덱스를 반환
        answer = arr.index(1, idx)
    except:
        # 만약 1이 존재하지 않으면 예외 발생 → -1 반환
        answer = -1
    return answer

if __name__ == "__main__":
    arr = [0, 0, 0, 1]
    idx = 1
    # arr[1:] = [0, 0, 1] → 처음 나오는 1은 인덱스 3
    print(solution(arr, idx))  # 출력: 3
    print(solution2(arr, idx))  # 출력: 3
