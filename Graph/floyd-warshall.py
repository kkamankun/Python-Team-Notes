"""
플로이드 워셜 알고리즘
All Source - All Destination
시간 복잡도: O(N^3)
"""

import sys

INF = int(1e9)

# 노드의 개수 및 간선의 개수를 입력받기
node = int(sys.stdin.readline().rstrip())
edge = int(sys.stdin.readline().rstrip())

# 2차원 리스트(그래프) 생성, 무한으로 초기화
graph = [[INF] * (node + 1) for _ in range(node + 1)]  # 인덱스 1부터 라고 가정해서 node + 1

# 자기 자신으로 가는 비용은 0으로 초기화 (대각 행렬 0으로 초기화)
for i in range(1, node + 1):
    for j in range(1, node + 1):
        if i == j:
            graph[i][j] = 0

# 주어진 입력 받아서 초기화
for _ in range(edge):
    src, des, weight = map(int, sys.stdin.readline().rstrip().split())
    graph[src][des] = weight
    # 양방향일 경우 아래 한 줄 추가
    # graph[des][src] = weight

# 점화식에 따라 floyd-warshall 알고리즘 수행
for k in range(1, node + 1):
    for i in range(1, node + 1):
        for j in range(1, node + 1):
            # k를 지나치는 경로와, 직접 가는 경로중 더 짧은 경로로 업데이트
            graph[i][j] = min(graph[i][j], graph[i][k], graph[k][j])

# 결과 출력
for i in range(1, node + 1):
    for j in range(1, node + 1):
        # 도달할 수 없는 경우
        if graph[i][j] == INF:
            print("무한", end=' ')
        else:
            print(graph[i][j], end=' ')
    print()
