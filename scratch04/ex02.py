"""
numpy package를 사용한 벡터 연산
"""
import numpy as np
from math import sqrt

print('numpy version: ', np.__version__)

# 두 벡터의 덧셈
v = [1, 2]  # class list
# print(type(v))
print('v = ', v)
w = [2, 3]
print('w = ', w)
print(v + w)
# print(v - w)  # 오류 발생 !!
# list는 + 연산을 사용할 수 있음
# + 연산자는 extend 함수와 비슷한 기능
# + 연산자는 v나 w를 변경하지 않고, 새로운 list를 리턴
# v.extend(w) 함수는 v를 변경함

# v가 새로운 w와 결합된 리스트로 변환됨
v.extend(w)
print(v)

# numpy 패키지의 ndarray 타입을 사용!
# n-dimensional array(n차원 배열)
v = np.array([1, 2])
print('type:', type(v))
print('dimension:', v.ndim)
print('shape: ', v.shape)

w = np.array([
    [1, 2],
    [3, 4]
])
print('type w: ', type(w))
print('dimension: ', w.ndim)
print('shape: ', w.shape)
x = np.array([
    [[1], [2]],
    [[3]]
])
print('type x: ', type(x))
print('dimension: ', x.ndim)
print('shape: ', x.shape)

# ndarray 타입을 이용한 벡터 연산
v = np.array([1, 2, 3])
w = np.array([3, 4, 5])
vector_add = v + w
print('vector add =', vector_add)  # 두 list를 옆에다 붙이는 것이 아니라, 벡터 연산을 함
vector_sub = v - w
print('vector subtract =', vector_sub)

vectors = np.array([
    [1, 2],
    [3, 4]
])
np_sum = np.sum(vectors)  # 2차원 배열 모든 원소들의 합
print('np_sum = ', np_sum)

np_sum_by_col = np.sum(vectors, axis=1)
print('np_sum_by_col =', np_sum_by_col)

np_mean = np.mean(vectors)
print(np_mean)
v = np.array([1, 2, 3])
scalar_mul = 3 * v

print('scalar multiplitcation = ', scalar_mul)
scalar_div = 3 / v
print('scalar division = ', scalar_div)
v = np.array([1, 2])
w = np.array([3, 4])
print('dot = 10', v.dot(w)) # v랑 w랑 내적


# numpy를 사용한 벡터의 크기
def norm(v):
    return sqrt(v.dot(v))

v = np.array([1, 1])
print('norm =', norm(v))

# numpy를 사용한 두 벡터간의 거리:
def dist(v, w):
    return norm(v - w)