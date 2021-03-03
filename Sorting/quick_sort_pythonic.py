''' 퀵 정렬(Quick Sort) 오름차순 정렬 '''
def quick_sort(li):  # 리턴이 있는 버전
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(li) <= 1:
        return li

    pivot = li[0]  # 피벗은 첫 번째 원소
    tail = li[1:]  # 피벗을 제외한 나머지
    
    left_side = [x for x in tail if x <= pivot]  # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot]  # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행, 전체 리스트 반환
    # + 연산을 통해 리스트 병합
    # 왼쪽, 오른쪽의 리스트를 각각 재귀적으로 연산
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
print(quick_sort(array))
