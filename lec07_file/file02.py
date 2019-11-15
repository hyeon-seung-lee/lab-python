"""
파일을 다루는 데 다음 순서를 준수해야 한다.
1) open file
2) read/write file
3) close file
"""
# 파일 열기(쓰기 모드)
f = open('test.txt', 'w', encoding='utf-8')

# 파일에 텍스트를 씀
for i in range(1, 11):
    f.write(f'{i}번째 줄 ...  \n')

# 파일 닫기
f.close()

# with 구문: 리소스를 사용한 후  close() 메소드를 자동으로 호출
# with  ...  as 변수:  실행문

with open('test2.txt', mode = 'w', encoding= 'utf-8') as f:
    f.write('Hello, Python\n')
    f.write('점심 식사는 맛있게 하셨나요?\n')
    f.write('0123456789\n')

