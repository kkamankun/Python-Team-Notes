''' 계수 정렬(Count Sort) 오름차순 정렬 '''
def count_sort(li):
    # 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
    count = [0] * (max(li) + 1)
    result = list()
    
    for num in li:
        count[num] += 1  # 데이터에 해당하는 인덱스의 값 증가
    
    for i in range(len(count)):  # 리스트에 기록된 정렬 정보 확인
        for j in range(count[i]):
            result.append(i)
    return result


array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
print(count_sort(array))
