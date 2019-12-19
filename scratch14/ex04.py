import numpy as np

# (2, 3) shape의 모든 원소가 1인 array를 생성해서 출력 : A
a = np.ones((2, 3), dtype=np.int)
# print(a)
# (2, 3) shape의 모든 원소가 0인 array를 생성해서 출력 : B
b = np.zeros((2, 3))
# print(b)
# (3, 2) shape의 모든 원소가 1 ~ 6인 array를 생성해서 출력 : C
c = np.arange(1, 7).reshape((3, 2))
# print(c)

# (3, 2) shape의 난수로 이루어진 array를 생성해서 출력 : D
d = np.random.randint(1, 7, (3, 2))
# print(d)

"""다음과 같은 결과가 나올 수 있도록 
numpy를 사용하지 않고 add(x, y), subtract(), multiply(), divide(), dot() 함수를 구현
|1 2| + |5 6|= |6  8 | 
|3 4|   |7 8|  |10 12|

|1 2| - |5 6|= |-4 -4| 
|3 4|   |7 8|  |-4 -4|

|1 2| * |5 6|= |5  12| 
|3 4|   |7 8|  |21 32|

|1 2| / |5 6|= |0.2   0.333| 
|3 4|   |7 8|  |0.428 0.5  |

|1 2| @ |5 6|= |19 22| 
|3 4|   |7 8|  |43 50|
위의 결과와 같은 결과를 주는 numpy 코드를 작성
"""


class Matrix():
    def __init__(self, matrix1, matrix2):
        """ matrix1, 2는 n * n 정사각행렬이라고 가정"""
        self.x = matrix1
        self.y = matrix2
        result = []
        for row in range(len(self.x)):
            temp = []
            for col in range(len(self.x[0])):
                temp.append(0)
            result.append(temp)
        self.result = result

    def add(self):
        for row in range(len(self.x)):
            for col in range(len(self.x[0])):
                self.result[row][col] = self.x[row][col] + self.y[row][col]
        return self.result

    def subtract(self):
        for row in range(len(self.x)):
            for col in range(len(self.x[0])):
                self.result[row][col] = self.x[row][col] - self.y[row][col]
        return self.result

    def multiply(self):
        for row in range(len(self.x)):
            for col in range(len(self.x[0])):
                self.result[row][col] = self.x[row][col] * self.y[row][col]
        return self.result

    def divide(self):
        for row in range(len(self.x)):
            for col in range(len(self.x[0])):
                self.result[row][col] = self.x[row][col] / self.y[row][col]
        return self.result

    def dot(self):
        for row in range(len(self.x)):
            for col in range(len(self.x[0])):
                for i in range(len(self.x[0])):
                    self.result[row][col] += self.x[row][i] * self.y[i][col]
        return self.result


x = [[1, 2], [3, 4]]
y = [[5, 6], [7, 8]]

matrix_calculation = Matrix(x, y)
print('add: ', matrix_calculation.add())
print('sub :', matrix_calculation.subtract())
print('mul :', matrix_calculation.multiply())
print('div :', matrix_calculation.divide())
print('dot :', matrix_calculation.dot())

np_x = np.array([[1, 2], [3, 4]])
np_y = np.array([[5, 6], [7, 8]])
print('np.add: \n', (np_x + np_y))
print('np.sub: \n', (np_x - np_y))
print('np.mul: \n', (np_x * np_y))
print('np.div: \n', (np_x / np_y))
print('np.dot: \n', np.dot(np_x, np_y))
print('np.dot: \n', np_x@np_y)

"""
항등 행렬(Indentity matrix): 대각선의 원소는 1이고, 나머지 원소는 0인 정사각행렬
    A @ I = I @ A = A를 만족
역행렬(Inverse matrix): A @ A- = A- @ A = I를 만족하는 행렬
전치 행렬(Transpose matrix): 행렬의 row와 column을 서로 바꾼 행렬
"""
# 항등 행렬
print(np.eye(2))
# 전치 행렬
print(np_x.transpose())
# 역행렬
print(np.linalg.inv(np_x))