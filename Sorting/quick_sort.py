# 리턴이 없는 버전
def quick_sort(li, start, end):
    if start >= end:        # 원소가 1개인 경우 종료
        return
    pivot = start           # 피벗은 첫 번째 원소
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and li[left] <= li[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and li[right] >= li[pivot]:
            right -= 1
        # 엇갈렸다면 피벗과 교체
        if left > right:
            li[right], li[pivot] = li[pivot], li[right]
        # 정상적인 상황이라면 left, right 교체
        else:
            li[left], li[right] = li[right], li[left]
    # 분할 이후 왼쪽 리스트, 오른쪽 리스트 각각 재귀
    quick_sort(li, start, right - 1)
    quick_sort(li, right + 1, end)


array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
quick_sort(array, 0, len(array) - 1)
print(array)
