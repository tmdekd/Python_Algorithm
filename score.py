# -*- coding: utf-8 -*-

# 테스트 케이스의 수를 입력받습니다.
T = int(input())

# 각 테스트 케이스를 처리합니다.
for test_case in range(1, T + 1):
    # 학생 수 n과 학점을 알고 싶은 학생 번호 k를 입력받습니다.
    n, k = map(int, input().split())

    # 학점을 부여할 리스트 정의
    grade_levels = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]

    # 모든 학생의 총점을 저장할 리스트
    scores = []

    # n명의 학생 점수를 입력받아 총점을 계산합니다.
    for i in range(n):
        mid, final, assignment = map(int, input().split())
        total_score = mid * 0.35 + final * 0.45 + assignment * 0.2
        scores.append([total_score, i + 1])  # 총점과 학생 번호를 함께 저장

    # 총점을 기준으로 내림차순 정렬
    scores.sort(reverse=True)

    # 각 학점당 인원 수
    students_per_grade = n // 10

    # 목표 학생의 학점을 찾습니다.
    result_grade = ""
    for idx, (score, student_no) in enumerate(scores):
        if student_no == k:
            # 학점을 계산하기 위해 인덱스에 해당하는 등급을 할당
            result_grade = grade_levels[idx // students_per_grade]
            break

    # 테스트 케이스 번호와 결과 학점을 출력합니다.
    print(f"#{test_case} {result_grade}")
