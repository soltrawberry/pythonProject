import numpy as np

# 기본 데이터
list =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr1 = np.array(list)
arr2 = np.array(list)

# 넘파이 제공 연산자 사용
print(arr1 + arr2)

# 모든 원소들을 직접 더하는 연산 수행 로직
arr3 = []

# for문을 사용해 arr1 + arr2를 구현
for i in range(1, 2, 1):
        arr3.append(arr1 + arr2)

print(arr3)