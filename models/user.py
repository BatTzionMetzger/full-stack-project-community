from models.db_queries import *

def is_exist(email):
    query = '''SELECT count(*) FROM user 
    WHERE mail = '{}' '''.format(email)
    res = select_query(query)
    if res[0].get('count(*)') > 0:
        return True
    return False

def insert(mail, password, name, community_id, phone):
    query=""
    if phone:
        query = """INSERT INTO user
        VALUES('{}', '{}', '{}', {}, '{}')""".format( mail, password, name, community_id, phone)
    else:
        query = """INSERT INTO user (mail, password, name, community_id)
        VALUES('{}', '{}', '{}', {})""".format( mail, password, name, community_id)
    succ = update_db_by_query(query)
    if succ:
        return True
    return False