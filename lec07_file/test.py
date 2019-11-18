import lec07_file.file07 as fl7
import os

file_name = os.path.join('data', 'exam.csv')
print(file_name)
print(file_name[1])
print(file_name[2])

# 별표 두 개(**)를 붙이는 경우
def fn(**args):
    pass

# 함수 호출시 argument의 키워드를 붙여주어야 함
fn(x = 1, y = 2)