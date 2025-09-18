# -*- coding: utf-8 -*-

# 10개의 테스트 케이스 처리
for t in range(1, 11):  # 10개의 테스트 케이스
    case = int(input())  # 테스트 케이스 번호 입력
    data = list(map(int, input().split()))  # 8개의 숫자를 입력받아 리스트로 저장

    cycle = 1  # 감소값을 설정할 사이클 초기화
    while True:
        # 리스트의 첫 번째 요소를 꺼내서 사이클 값만큼 감소
        first = data.pop(0)
        first -= cycle

        # 감소된 값이 0 이하인 경우 0으로 설정하고 리스트 마지막에 추가, 종료
        if first <= 0:
            data.append(0)  # 0을 맨 뒤에 추가하여 암호 완성
            break
        else:
            data.append(first)  # 감소된 값을 맨 뒤에 추가

        # 사이클 값 1, 2, 3, 4, 5를 반복 (5 이후 다시 1로 돌아감)
        if cycle == 5:
            cycle = 1  # 사이클을 다시 1로 초기화
        else:
            cycle += 1  # 사이클 값을 1 증가

    # 결과 출력 (테스트 케이스 번호와 리스트 값들을 출력)
    print(f"#{case}", *data)
