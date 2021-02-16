# 맨하탄 거리 구하는 함수

def manhattan_distance(pt1, pt2):
    result = 0
    for i in range(len(pt1)):
        result += abs(pt2[i] - pt1[i])
    return result
