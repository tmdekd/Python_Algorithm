"""
백준 1546번: 평균 (성공 스페셜 저지)

[문제 설명]
- 세준이는 기말고사 점수를 조작하기로 했다.
- 자신의 점수 중 최댓값 M을 기준으로, 각 점수를 (점수 / M * 100) 으로 고친다.
- 이렇게 바뀐 점수들의 평균을 구하는 프로그램을 작성한다.

[입력]
- 첫째 줄: 시험 본 과목의 개수 N (1 ≤ N ≤ 1000)
- 둘째 줄: 현재 성적 (각 점수는 0 이상 100 이하의 정수, 적어도 하나는 0보다 큼)

[출력]
- 새로 계산한 점수들의 평균을 출력한다.
- 실제 정답과 출력값의 절대오차 또는 상대오차가 10^-2 이하이면 정답 처리된다.

[예제 입력 1]
3
40 80 60

[예제 출력 1]
75.0

[예제 입력 2]
3
10 20 30

[예제 출력 2]
66.666667

※ "10^-2 이하의 오차 허용"은 반드시 소수 둘째 자리까지만 출력하라는 의미가 아님.
"""
n = int(input())
scores = list(map(int, input().split(' ')))
max_score = max(scores)
new_scores = []

for score in scores:
    new_score = score / max_score * 100
    new_scores.append(new_score)
    
print(sum(new_scores) / n)

# 위의 방법과 아래의 방법 모두 사용 가능

n = int(input())
scores = list(map(int, input().split(' ')))
max_score = max(scores)

sum = sum(scores)    
print(sum * 100 / max_score / n)