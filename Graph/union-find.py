"""
서로소 집합 알고리즘: Union-Find
두 서브트리를 계속 합치며 공통원소 파악
시간 복잡도: O(VM) -> V는 vertex 개수, M 은 union & find 연산의 개수
"""


# find 연산: 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x


# union 연산: 두 원소가 속한 집합을 합치기, 두 서브 트리 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 노드의 개수와 간선의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v + 1)      # 부모 테이블 초기화

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소의 루트 노드 출력 (집합 구분)
print("각 원소가 속한 집합(루트 노드): ", end='')
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')

print()
# 부모 테이블 출력
print("부모 테이블: ", end='')
for i in range(1, v+1):
    print(parent[i], end=' ')
