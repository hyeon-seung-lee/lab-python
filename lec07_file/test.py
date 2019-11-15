import lec07_file.file07 as fl7
import os

file_name = os.path.join('data', 'exam.csv')
exam_data = fl7.my_csv_reader(file_name)


a = exam_data[0].replace(" ","").split(',')
print(a)
