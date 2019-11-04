"""
파이썬 데이터 타입:
숫자 타입 : int(정수), float(실수), complex(복소수)
논리 타입 : bool(True, False)
문자열: str
시퀀스(Sequence): list, tuple
매핑(mapping): dict
집합: set
"""

intVal = 123
print(type(intVal))
print(id(intVal))

floatVal = 3.141592
print(type(floatVal))

complexVal = 1 + 2j
print(type(complexVal))
print(1j**2)

#bool
result = 10 > 2
print(result)
print(type(result))

str1 = 'abc'
print(type(str1))

name = None
print(type(name))
