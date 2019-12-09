from bs4 import BeautifulSoup

with open('web02.html', mode='r', encoding='UTF-8') as f:
    soup = BeautifulSoup(f, 'html5lib')
    # print(soup)

    # HTML 문서 안의 모든 div 태그를 찾음
    for div in soup.find_all('div'):  # soup('div')와 soup.find_all('div')는 동일한 기능
        print(div.text)
    print('-------------------')
    # HTML 문서 안의 'class1' 클래스 속성을 갖는 모든 요소들을 찾음
    # soup(attrs = {attr이름: attr값})
    # soup.find_all(attrs={attr이름:attr값})
    for class1 in soup(attrs={'class': 'class1'}):
        print(class1)
    for class1 in soup.find_all(attrs={'class': 'class1'}):
        print(class1)
    print('xxxxxxxxxxxxxx')
    # HTML 문서 안의 'class2' 클레스 속성을 갖는 모든 요소들을 찾음
    for cls2 in soup.find_all(id= 'id1'):
        print(cls2.text)