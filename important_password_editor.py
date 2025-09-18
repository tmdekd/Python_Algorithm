# -*- coding: utf-8 -*-

t = 10  # 총 10개의 테스트 케이스
for test in range(1, t+1):  # 각 테스트 케이스에 대해 반복
    n = int(input())  # 암호문의 개수 입력 받음
    arr = list(map(int, input().split()))  # 원본 암호문 뭉치를 리스트 형태로 저장
    m = int(input())  # 명령어의 개수 입력 받음
    cmd = list(input().split())  # 명령어를 리스트 형태로 저장

    # 명령어 리스트(cmd)에서 각 명령어를 순회하며 처리
    for i in range(len(cmd)):
        # 삽입 명령어('I') 처리
        if cmd[i] == 'I':
            # cmd[i+1]: 삽입 위치 x, cmd[i+2]: 삽입할 암호문의 개수 y
            for j in range(int(cmd[i+2])):  # y만큼 반복하여 삽입할 암호문 처리
                # x+j 위치에 삽입, 삽입할 암호문은 cmd[i+3+j]
                arr.insert(int(cmd[i+1]) + j, int(cmd[i+3 + j]))

        # 삭제 명령어('D') 처리
        elif cmd[i] == 'D':
            # cmd[i+1]: 삭제 시작 위치 x, cmd[i+2]: 삭제할 개수 y
            del arr[int(cmd[i+1]):int(cmd[i+1]) + int(cmd[i+2])]  # x부터 x+y 위치까지 삭제

        # 추가 명령어('A') 처리
        elif cmd[i] == 'A':
            # cmd[i+1]: 추가할 암호문의 개수 y
            y = int(cmd[i + 1])  # 추가할 암호문의 개수

            # cmd[i+2]부터 시작해서 y개의 암호문을 리스트 끝에 추가
            for j in range(y):
                s_value = int(cmd[i + 2 + j])  # 각 암호문 값을 정수로 변환
                arr.append(s_value)  # 리스트 arr의 끝에 암호문 추가

    # 결과 출력: 수정된 암호문 뭉치의 앞 10개만 출력
    print(f"#{test}", end=" ")  # 테스트 케이스 번호를 출력하고 줄바꿈 없이 유지

    # 처음 10개의 요소를 하나씩 출력
    for k in range(10):
        print(arr[k], end=" ")  # 각 요소를 공백으로 구분하여 출력
    print()  # 각 테스트 케이스가 끝나면 줄바꿈
