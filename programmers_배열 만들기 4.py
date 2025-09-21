def solution(arr):
    stk = []
    i = 0
    while i < len(arr):
        if len(stk) == 0:
            stk.append(arr[i])
            i += 1
        elif len(stk) > 0 and stk[-1] < arr[i]:
            stk.append(arr[i])
            i += 1
        elif len(stk) > 0 and stk[-1] >= arr[i]:
            del stk[-1]
    return stk

if __name__ == "__main__":
    arr = [1, 4, 2, 5, 3]
    print(solution(arr))  # [1, 2, 3]