# Insertion Sort 오름차순 정렬

def insertion_sort(li):
    li_len = len(li)   # 1차원 리스트 길이
    for i in range(1, li_len):
        for j in range(i, 0, -1):  # 현재위치부터 왼쪽으로 이동하며 탐색
            if li[j] < li[j-1]:    # 한칸씩 왼쪽으로 이동
                li[j], li[j - 1] = li[j - 1], li[j]  # 이동을 swap 으로 구현
            else:    # 자신보다 작은 데이터를 만나면 그 위치에서 멈춤
                break


print(insertion_sort([7, 5, 9, 0, 3, 1, 6, 2, 4, 8]))
