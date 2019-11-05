"""
dict: key-value의 쌍으로 이루어진 데이터들을 저장하는
사전(dictionary)식 데이터 타입
"""

person = {'name': '모쌤', 'age': 16, 'height': 170.5 }
print(person)
print(type(person))


# dict의 데이터 참조 - key 이용
print(person['name'])
print(person['age'])

# dict의 key를 알아낼 때
print(person.keys())
# dict의 value를 알아낼 때
print(person.values())

# key와 value를 출력할 때
print(person.items())


students = {1: '강다혜', 2: '김수인', 3: '김영광'}
print(students[1])

# dict에 값을 추가
students[4] = '김제성'
print(students[1])

# dict의 값을 변경 -- 기존의 key 값을 이용
students[4] = '김길동'
print(students)

#dict의 값을 삭제 -- pop
students.pop(4)
print(students)

book = {
    'title' : '파이썬 프로그래밍 교과서',
    'authors' : ['제니퍼', '폴', '제이슨'],
    'publisher' : '길벗',
    'isbn' : 97911
}
print(book['authors'][0])
print(book['authors'])