# open
f = open('test.txt', mode='r', encoding='utf-8')
# read: read(), readline()111
# content = f.read()  # 텍스트 문서 전체를 읽음
content = f.read(3)  # read(n): n개의 문자만 읽음
print(content)
content = f.read(3)  # read(n): n개의 문자만 읽음
print(content)
# close
f.close()

f = open('test2.txt', mode='r', encoding='utf-8')

line = f.readline()
line = line.strip()          # 기존 line을 strip type로 저장(한 줄로)
print(f'line: {line}, length: {len(line)}')
line = f.readline().strip()  # 위 결과를 한 줄로 입력
print(f'line: {line}, length: {len(line)}')
f.close()


print('                  \t          hello            \t\n     ')
print('                  \t          hello            \t\n     '.strip())


f = open('test.txt', mode = 'r', encoding= 'utf-8')
line = f.readline()
while line:
    # line이 빈 문자열이면 False, 그렇지 않으면 True
    print(line.strip())
    line = f.readline()

f.close()

line = []
with open('test2.txt', mode = 'r', encoding='utf-8') as f:
    line = f.readline()
    while line:
        print(line.strip())
        line = f.readline()
f.close()
