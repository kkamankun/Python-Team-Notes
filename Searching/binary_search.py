# 이진 탐색
# 리스트가 li로 주어졌고, 찾고자 하는 값이 target 으로 주어졌을 때
# start, end 를 통해 mid 를 구하고 범위를 반으로 좁혀가며 탐색
# O(logN): 평균적으로 log_2(N)

# 바이너리 서치 - 재귀함수
def binary_search(li, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 인덱스 반환
    if li[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽:
    elif li[mid] > target:
        return binary_search(li, target, start, mid - 1)
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 오른쪽:
    else:
        return binary_search(li, target, mid + 1, end)


# 바이너리 서치 - 반복문
def binary_search_loop(li, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if li[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif li[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 오른쪽 확인
        else:
            start = mid + 1
    return None
