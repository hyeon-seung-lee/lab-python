"""
numpy의 행렬 관련 함수
"""
import numpy as np

# numpy.ndarray 타입의 객체를 생성
A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

B = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])
print(A)
print(B)

print(A.shape)
print(B.shape)
nrows, ncols = B.shape
print(nrows, 'x', ncols)

# slicing: 특정 행, 특정 열의 원소들을 추출하는 방법
# list[i][j], ndarray[i, j]
print(A[0, 0])
print(B[1, 1])
print(A[0:2, 0:3])
print('3', A[0, :]) # index 0번 column의 원소들로 이루어진 array
print(A[:, 0]) # index 0번 row의 원소들로 이루어진 array
print(B[1, 0:2])
print(B[:, 0:2])

# 항등 행렬(Identity Matrix)
identity_matrix = np.identity(3, dtype=int)
print(identity_matrix)

# 전치 행렬(Transpose Matrix)
print(A.transpose())

# 행렬 곱셈 : dot함수
print(A.dot(B))
print(B.dot(A))