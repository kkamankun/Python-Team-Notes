"""
크루스칼(Kruskal) 알고리즘
최소 비용 신장 트리(Minimum Spanning Tree)를 구하는 알고리즘
그리디 기반
시간 복잡도: O(ElogE)
"""
import sys


# find 연산 - 경로 압축법
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# union 연산
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 기본 입력
v, e = map(int, sys.stdin.readline().rstrip().split())
parent = [0] * (v + 1)

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블 루트 노드 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i


# 기본 입력
for _ in range(e):
    a, b, cost = map(int, sys.stdin.readline().rstrip().split())
    # 비용 순으로 edge 정렬하기 위해 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost, a, b))

# 간선을 비용 순으로 정렬
edges.sort()

# 간선을 하나씩 확인
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)
