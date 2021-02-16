# Selection Sort 오름차순 정렬

def selection_sort(li):   # 파라미터로 1차원 리스트
    li_len = len(li)      # 리스트의 길이
    for i in range(li_len):
        min_idx = i       # 가장 왼쪽 인덱스 저장
        for j in range(i+1, li_len):  # 가장 작은 원소의 인덱스 탐색
            if li[min_idx] > li[j]:   # 탐색하며 업데이트
                min_idx = j
        # 가장 작은 원소와 스왑
        li[i], li[min_idx] = li[min_idx], li[i]
    return li


print(selection_sort([7, 5, 9, 0, 3, 1, 6, 2, 4, 8]))
