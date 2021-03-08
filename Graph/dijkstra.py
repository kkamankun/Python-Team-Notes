import sys

INF = int(1e9)

# 노드의 개수, 간선의 개수를 입력받기
node, edge = map(int, sys.stdin.readline().rstrip().split())

# 시작 노드 입력받기
start = int(sys.stdin.readline().rstrip())

# 그래프 생성, 방문 노드 체크 리스트 생성, 최단거리 테이블 생성 및 무한으로 초기화
graph = [[] for _ in range(node + 1)]
visited = [False] * (node + 1)
distance = [INF] * (node + 1)

# 모든 간선 정보 입력받기
for _ in range(edge):
    src, des, weight = map(int, sys.stdin.readline().rstrip().split())
    graph[src].append((des, weight))


def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, node + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def dijkstra(start):
    # 시작 노드 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n-1 개의 노드에 대해 반복
    for i in range(node-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for adj_node in graph[now]:
            cost = distance[now] + adj_node[1]
            # 기존 값보다 더 짧은 경우
            if cost < distance[adj_node[0]]:
                distance[adj_node[0]] = cost


dijkstra(start)

# 결과 출력
for i in range(1, node + 1):
    if distance[i] == INF:
        print("무한")
    else:
        print(distance[i])
