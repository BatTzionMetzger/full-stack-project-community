from models.db_queries import *

def insert(name, password, admin_mail, img_path):
    query=""
    if img_path:
        query = """INSERT INTO community (name, password, admin_mail, img_path) 
        VALUES('{}', '{}', '{}', '{}')""".format( name, password, admin_mail, img_path)
    else:
        query = """INSERT INTO community (name, password, admin_mail) 
        VALUES('{}', '{}', '{}')""".format( name, password, admin_mail)
    succ = update_db_by_query(query)
    if succ:
        return True
    return False

def is_exist(id_, password):
    query = '''SELECT count(*) FROM community 
    WHERE id = {} and  password = '{}' '''.format(id_, password)
    res = select_query(query)
    if res[0].get('count(*)') > 0:
        return True
    return False
