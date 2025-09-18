# -*- coding: utf-8 -*-
from collections import deque # 큐를 구현하여 선입선출

T = int(input())  # 테스트 케이스 개수

for t in range(1, T + 1):
    v, e = map(int, input().split())  # 노드와 간선의 개수 입력
    graph = {}  # 그래프 초기화

    # 노드 초기화
    for i in range(1, v + 1):
        graph[i] = []  # 각 노드에 대한 빈 리스트 생성

    # 간선 정보 입력
    for _ in range(e):
        start, end = map(int, input().split())
        # 즉, 딕셔너리의 키와 연결된 노드들이 value가 된다.
        graph[start].append(end)

    # 출발 노드와 도착 노드 입력
    s, g = map(int, input().split())

    # BFS로 경로 탐색
    queue = deque([s])  # 시작 노드를 큐에 추가
    visited = [False] * (v + 1)  # 방문 확인용 배열 (노드 번호 1부터 시작하므로 v+1 크기로 초기화)
    found = 0  # 경로 존재 여부 (0: 없음, 1: 있음)

    while queue:  # 큐가 비어 있지 않는 동안 반복
        node = queue.popleft()  # 큐에서 노드를 꺼냄
        if node == g:  # 목표 노드에 도달하면
            found = 1
            break
        if not visited[node]:  # 방문하지 않은 노드라면
            visited[node] = True  # 방문 처리
            for neighbor in graph[node]:  # 인접 노드들을 순회하며 큐에 추가
                if not visited[neighbor]:
                    queue.append(neighbor)

    # 결과 출력
    print(f"#{t} {found}")
