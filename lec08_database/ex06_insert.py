"""
ex06_insert.py

사용자 입력을 받아서 데이터베이스에 insert
"""
import cx_Oracle
import lec08_database.oracle_config as cfg

with cx_Oracle.connect(cfg.user, cfg.pwd, cfg.dsn) as connection:
    with connection.cursor() as cursor:
        deptno = int(input('부서번호 입력>>'))
        dname = input('부서이름 입력>>')
        loc = input('부서위치 입력>>')

        sql_insert = f"insert into dept2 values({deptno}, '{dname}', '{loc}')"
        # 사용자가 입력한 문자열에 따옴표(')나 큰따옴표(")가 포함되어 있는 경우
        # SQL 에러가 발생할 수 있으므로 권장되지 않음.
        # -> Data Binding 방법을 권장.
        cursor.execute(sql_insert)
        connection.commit()
        sql_query = 'select * from dept2'
        cursor.execute(sql_query)
        for row in cursor:
            print(row)

