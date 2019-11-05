"""
tuple(튜플): 원소(값)들을 변경할 수 없는 리스트
"""

numbers = (1,2,3)
print(numbers)
print(numbers[0]) # 인덱스
print(numbers[0:2]) # 슬라이싱
one, two, three = numbers   # decompostiion
print(one, two, three)

# numbers[0] = 1 # 튜플은 변경 불가능