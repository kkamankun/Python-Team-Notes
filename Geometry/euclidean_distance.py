# 유클리드 거리 구하는 함수
def euclidean_distance(pt1, pt2):
    result = 0
    for i in range(len(pt1)):
        result += (pt2[i] - pt1[i]) ** 2
    return result ** 0.5
