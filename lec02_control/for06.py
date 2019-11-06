"""
dictionary comprehension
"""

numbers = [1, 2, 3, 4, 5]
names = ['tiger', 'rabbit', 'frog', 'lion', 'noguri']

animals = {} # empty dict
for i in range(len(numbers)):
    animals[numbers[i]] = names[i]
print(animals)

# dictionary comprehension
animals2 = {numbers[i]: names[i]
            for i in range(len(numbers))}
print(animals2)

# dict를 만들어주는 함수 zip
num_name = zip(numbers, names)
print(num_name)

for x in zip(numbers, names):
    print(x)

students3 = {}
for key, value in zip(numbers, names):
    students3[key]= value
print(students3)

students4 = {k: v for k, v in zip(numbers, names)}
print(students4)

students5 = {k:v
             for k, v in zip(numbers, names)
             if k%2} # 0은 false, 다른 숫자는 true -> 홀수를 출력하는 문장. k%2 == 1 과 같다.
                     # 짝수를 출력할 때, k%2==0에서 생략할 수 없다.
print(students5)


