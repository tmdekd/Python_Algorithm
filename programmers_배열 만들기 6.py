def solution(arr):
    answer = []
    i = 0
    while i < len(arr):
        if len(answer) == 0:
            answer.append(arr[i])
            i += 1
        elif len(answer) > 0 and answer[-1] == arr[i]:
            del answer[-1]
            i += 1
        elif len(answer) > 0 and answer[-1] != arr[i]:
            answer.append(arr[i])
            i += 1
    return answer if answer else [-1]

if __name__ == "__main__":
    arr = [0, 1, 1, 1, 0]
    print(solution(arr))  # [0, 1, 0]