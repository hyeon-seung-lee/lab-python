"""
ex08_ update.py
수정할 deptno, 수정할 loc를 입력받아서 loc만 변경 update

"""
import cx_Oracle
import lec08_database.oracle_config as cfg

with cx_Oracle.connect(cfg.user, cfg.pwd, cfg.dsn) as connection:
    with connection.cursor() as cursor:
        deptno = int(input('변경된 부서번호 입력: '))
        loc = input('변경된 부서 위치 입력 :')
        adjust_query = 'update dept2 set loc = :ad_loc where deptno = :ad_deptno'
        cursor.execute(adjust_query, ad_loc = loc, ad_deptno = deptno)
        connection.commit()

