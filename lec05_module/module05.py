"""
module05.py
"""
#from utils import *
# from 패키지 import * 에서 import되는 모듈 이름들은
# 패키지 폴더의 __init__.py 파일의 __all__ 변수에 설정된 모듈 이름들임

# print(mymath01.pi)
# print(mymath02.multiply(11, 12))

# import 패키지 구문을 사용하면
# 패키지 폴더의 __init__.py 파일에서 미리 import한 모듈 이름들을 사용할 수 있음
import utils
print(utils.mymath02.divide(1,2))