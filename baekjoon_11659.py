"""
백준 11659번: 구간 합 구하기 4

[문제 설명]
- N개의 수가 주어진다.
- 이후 M번에 걸쳐, i번째 수부터 j번째 수까지의 합을 구하는 프로그램을 작성한다.

[입력]
- 첫째 줄: 수의 개수 N (1 ≤ N ≤ 100,000), 합을 구해야 하는 횟수 M (1 ≤ M ≤ 100,000)
- 둘째 줄: N개의 수 (각 수는 1,000 이하의 자연수)
- 셋째 줄부터 M개의 줄: 구간 [i, j] (1 ≤ i ≤ j ≤ N)

[출력]
- 총 M개의 줄에 각 구간 [i, j]의 합을 출력한다.

[제한]
- 1 ≤ N ≤ 100,000
- 1 ≤ M ≤ 100,000
- 1 ≤ i ≤ j ≤ N

[예제 입력]
5 3
5 4 3 2 1
1 3
2 4
5 5

[예제 출력]
12
9
1
"""
# n, m = list(map(int, input().split(' ')))
# array = list(map(int, input().split(' ')))

# for i in range(m):
#     start, end = list(map(int, input().split(' ')))
#     print(sum(array[start - 1:end]))
    
    
# 위의 방법과 아래의 방법 모두 사용 가능. 그러나 위의 방법은 '시간 초과' 발생
# 아래의 방법은 '시간 초과' 발생하지 않음
# Prefix Sum(누적 합) 활용

suNo, quizNo = map(int, input().split())
numbers = list(map(int, input().split()))
prefix_sum = [0]
temp = 0

# Prefix Sum(누적 합) 활용
# 합 배열 공식 : S[i] = S[i-1] + A[i]
for i in numbers:
    temp += i
    prefix_sum.append(temp)

# print(prefix_sum)
    
# 구간 합 공식 : S[J] - S[I-1]
for i in range(quizNo):
    start, end = map(int, input().split())
    print(prefix_sum[end] - prefix_sum[start - 1])