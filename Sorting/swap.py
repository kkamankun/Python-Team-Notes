# 0 인덱스와 1 인덱스의 원소 교체하기
def swap(array):
  array[0], array[1] = array[1], array[0]
  return array

print(swap([3, 5]))
