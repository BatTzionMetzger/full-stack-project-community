import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="nbm14916",
    db="community_db",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)


def update_db_by_query(query_str):
    with connection.cursor() as cursor:
        cursor.execute(query_str)
        connection.commit()
        return True

def select_query(query_str):
    with connection.cursor() as cursor:
        cursor.execute(query_str)
        result = cursor.fetchall()
        return result