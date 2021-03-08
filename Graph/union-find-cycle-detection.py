# find 연산 - 경로 압축법
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
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


# 기본 입력 받기
v, e = map(int, input().split())
parent = [0] * (v + 1)

# 부모 테이블에서 루트 노드를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# 사이클 발생 여부 flag
cycle = False

for i in range(e):
    a, b = map(int, input().split())
    # 사이클이 여부 판별 -> 발생시 종료
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    else:       # 발생하지 않았다면 union 연산 수행
        union_parent(parent, a, b)

if cycle:
    print("사이클 발생")
else:
    print("사이클 x")
