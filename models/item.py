from models.db_queries import *
# from db_queries import *

# def is_exist(email):
#     query = '''SELECT count(*) FROM item 
#     WHERE mail = '{}' '''.format(email)
#     res = select_query(query)
#     if res[0].get('count(*)') > 0:
#         return True
#     return False

def insert(name, description,img_path, owners_mail):
    query = """INSERT INTO item (name, description,img_path, owners_mail)
    VALUES('{}', '{}', '{}', '{}')""".format(name, description,img_path, owners_mail)
    succ = update_db_by_query(query)
    if succ:
        return True
    return False

def buy(item_id, user_email):
    query = """UPDATE item 
                SET is_available = 0, ordered_by_mail = '{}'
                WHERE id = {} """.format(user_email, item_id)
    succ = update_db_by_query(query)
    if succ:
        return True
    return False
