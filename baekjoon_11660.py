"""
백준 11660번: 구간 합 구하기 5

[문제 설명]
- N×N 표에 자연수가 채워져 있다.
- 쿼리 (x1, y1) ~ (x2, y2)의 부분합을 여러 번 빠르게 구하는 프로그램을 작성한다.
- (x, y)는 x행 y열(1-based)을 의미한다.

[입력]
- 첫째 줄: 표의 크기 N (1 ≤ N ≤ 1024), 쿼리 수 M (1 ≤ M ≤ 100,000)
- 다음 N줄: 각 행의 N개 정수 (각 수는 1 이상 1000 이하)
- 다음 M줄: x1 y1 x2 y2 (1 ≤ x1 ≤ x2 ≤ N, 1 ≤ y1 ≤ y2 ≤ N)

[출력]
- 총 M줄에 걸쳐 각 쿼리 구간의 합을 출력한다.

[예제 입력 1]
4 3
1 2 3 4
2 3 4 5
3 4 5 6
4 5 6 7
2 2 3 4
3 4 3 4
1 1 4 4

[예제 출력 1]
27
6
64

[예제 입력 2]
2 4
1 2
3 4
1 1 1 1
1 2 1 2
2 1 2 1
2 2 2 2

[예제 출력 2]
1
2
3
4

"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = [[0] * (n + 1)]
D = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(n):
    A_row = [0] + [int(x) for x in input().split()]
    A.append(A_row)
    
for i in range(1, n + 1):
    for j in range(1, n + 1):
        # 합 배열 공식
        D[i][j] = D[i][j - 1] + D[i - 1][j] - D[i - 1][j - 1] + A[i][j]
        
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    
    # 구간 합 공식
    result = D[x2][y2] - D[x1 - 1][y2] - D[x2][y1 - 1] + D[x1 - 1][y1 - 1]
    
    print(result)