"""
백준 1253번: '좋은 수' 구하기

[문제 설명]
- N개의 수 중에서 어떤 수가 다른 두 수의 합으로 나타낼 수 있다면 그 수를 "좋은 수(GOOD)"라고 한다.
- 주어진 N개의 수 중에서 "좋은 수"인 수의 개수를 구하는 프로그램을 작성한다.
- 단, 수의 위치가 다르면 값이 같아도 다른 수로 취급한다.

[입력]
- 첫째 줄: 수의 개수 N (1 ≤ N ≤ 2,000)
- 둘째 줄: N개의 정수 A1, A2, ..., AN (|Ai| ≤ 1,000,000,000)

[출력]
- "좋다"인 수의 개수를 출력한다.

[예제 입력 1]
10
1 2 3 4 5 6 7 8 9 10

[예제 출력 1]
8

[힌트]
- 3, 4, 5, 6, 7, 8, 9, 10은 다른 두 수의 합으로 나타낼 수 있으므로 "좋은 수"이다.
"""
import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
array.sort()

count = 0

for k in range(n):
    find = array[k]
    i = 0
    j = n - 1
    
    while i < j:
        if array[i] + array[j] == find:
            if i != k and j != k:
                count += 1
                break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1
        elif array[i] + array[j] < find:
            i += 1
        else:
            j -= 1
            
print(count)
    