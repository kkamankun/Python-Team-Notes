''' 퀵 정렬(Quick Sort) 오름차순 정렬 '''
def quick_sort(li, start, end):  # 리턴이 없는 버전
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
        if left > right:  # 엇갈렸다면 작은 데이터와 피벗을 교체
            li[right], li[pivot] = li[pivot], li[right]
        else:  # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            li[left], li[right] = li[right], li[left]
    # 분할 이후 왼쪽 리스트, 오른쪽 부분에서 각각 정렬 수행(재귀)
    quick_sort(li, start, right - 1)
    quick_sort(li, right + 1, end)


array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
quick_sort(array, 0, len(array) - 1)
print(array)
