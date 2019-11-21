"""
2차원 리스트(list)를 이용한 행렬
행렬의 Shape: (행x열)로 나타냄 !!
"""


def shape(matrix):
    """
    행렬의 행과 열의 개수를 tuple 형태로 return하는 함수
    :param matrix: 행렬
    (행의 갯수가 n개이고 열의 갯수가 m개인 2차원 리스트)
   :return:tuple (n, m)
    """
    n = len(matrix)  # 행의 개수
    m = len(matrix[0])  # 열의 개수
    return n, m


def get_row(matrix, index):
    """
    주어진 행렬(matrix)에서 index에 해당하는 row를 리턴
    :param matrix: n x m 행렬
    :param index: 행 번호
    :return: 벡터(원소가 m 개인 1차원 리스트)
    """
    return matrix[index - 1]


def get_column(matrix, index):
    """
        주어진 행렬(matrix)에서 index에 해당하는 column를 리턴
        :param matrix: n x m 행렬
        :param index: 열 번호
        :return: 벡터(원소가 n 개인 1차원 리스트)
        """

    x = []
    for m in matrix:
        x.append(m[index - 1])
    return x
    # return [x[index - 1] for x in matrix]


def make_matrix(nrows, ncols, fn):
    """
    함수의 리턴값들로 이루어진 nrows x ncols 행렬을 생성

    :param nrows: 행의 개수
    :param ncols: 열의 개수
    :param fn: 함수(fn(nrows, ncols) = 숫자)
    :return: nrows x ncols 행렬
    """
    rows = []
    matrix = []

    for i in range(nrows):
        for j in range(ncols):
            rows.append(fn(i, j))
        matrix.append(rows)

        rows = []
    # return matrix
    return [[fn(i, j) for j in range(ncols)] for i in range(nrows)]


def transpose(matrix):
    """
    주어진 행렬에서 행과 열을 뒤바꾼 행렬(전치 행렬)을 리턴
    :param matrix: matrix: n x m 행렬
    :return: m x n 행렬
    """
    rows = []
    trans_matrix = []
    nrows = len(matrix)
    ncols = len(matrix[0])

    for i in range(ncols):
        for j in range(nrows):
            rows.append(matrix[j][i])
        trans_matrix.append(rows)
        rows = []

    # return trans_matrix
    return [[matrix[j][i] for j in range(nrows)] for i in range(ncols)]


def transpose2(matrix):
    """
    주어진 행렬에서 행과 열을 뒤바꾼 행렬(전치 행렬)을 리턴
    ※ get_column 함수를 이용
    :param matrix: matrix: n x m 행렬
    :return: m x n 행렬
    """
    x = []
    n, m = shape(matrix)
    for i in range(m):
        x.append(get_column(matrix, i + 1))
    return x
    # return [get_column(matrix, i+1) for i in range(m)]


def transpose3(matrix):
    nrows, ncols = shape(matrix)
    t = make_matrix(ncols, nrows, lambda x, y: matrix[y][x])
    return t


if __name__ == '__main__':
    # 2x3 행렬(row=2, col=3)
    A = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    # 3x2 행렬(row=3, col=2)
    B = [
        [1, 2],
        [3, 4],
        [5, 6]
    ]
    print(A)
    print(B)

    print('Shape of A :', shape(A))
    print('Shape of B :', shape(B))

    print(get_column(A, 1))
    print(get_row(B, 1))

    print(make_matrix(3, 5, lambda x, y: 1))
    print(transpose(A))
    print(transpose2(A))
    print(transpose3(A))

    a = [1, 2, 3]
    b = [4, 5, 6]
    c = [7, 8, 9]

    for x, y, z in zip(a, b, c):
        print(x, y, z)

    # unpacking 연산자: *
    print('A =', A)
    print('*A =', *A)
    print('B =', B)
    print('*B =', *B)

    def transpose(matrix):
        print('unpacking 연산자 *를 사용한 transpose')
        t = []
        for col in zip(*matrix):
            print(col)
            t.append(col)
        return t
        return [list(x) for x in zip(*matrix)]
    print(transpose(A))
