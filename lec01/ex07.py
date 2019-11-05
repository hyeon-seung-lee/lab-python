"""
list : 여러 개의 값들을 하나의 변수에 저장하기 위한 데이터 타입
원소(element): 리스트에 저장된 값
인덱스(index): 리스트에 값이 저장된 위치(번호)
리스트의 원소들을 변경(추가/삭제) 가능
"""

numbers = [1, 2, 3, 4, 5, 'hello']
print(numbers[5]) # 리스트의 마지막 인덱스 = 리스트의 길이 - 1

# 범위 연산자를 이용한 slicing
print(numbers[3:5])

# 배열에 저장된 값(원소)을 변경
numbers[0] = 100
print(numbers)

# 배열에 원소 추가(append)
numbers.append('bye')
print(numbers)

# 배열에 원소 추가2(extend)
numbers.extend(['my', 'favorite', 7])
print(numbers)

# append와 extend 비교
numbers.append([8,9,10])
print(numbers)

# 원소 삭제 (remove): 값으로 삭제
numbers.remove(100)
print(numbers)

# 원소 삭제 (del): 인덱스로 삭제
del numbers[2]
print(numbers)

# 비어있는 리스트 만들기
empty = []
print(empty)

# 파이썬의 리스트는 여러가지 타입의 값들을 함께 저장할 수 있음.

person = ['모딩', 20, 175.6, True]
print(person[3], type(person[3]))

# list decomposition
name, age, height, marriage =  person
print(name, age, height, marriage)

# 2차원 리스트

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix)


print(matrix[0], type(matrix[0]))
print(matrix[0][2])
print(matrix[0:2][0])
print(matrix[0:2][1][1])

