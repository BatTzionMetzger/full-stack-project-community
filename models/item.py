from models.db_queries import *
import  models.user as user
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


def  get_item_by_owber(user_email):
    community_id = user.get_community_id_of_user(user_email)
    items_query = '''SELECT i.name as name, i.id as id , i.img_path as img_path, i.description as description
                FROM user as u JOIN item as i ON i.owners_mail = u.mail
                WHERE mail = '{}' and u.community_id = {} and i.is_available = 1'''.format(user_email, community_id)  
    res_items = select_query(items_query) 
    return res_items


def buy(item_id, user_email):
    query = """UPDATE item 
                SET is_available = 0, ordered_by_mail = '{}'
                WHERE id = {} """.format(user_email, item_id)
    succ = update_db_by_query(query)
    if succ:
        return True
    return False

def get_item_details(item_id):
    query = "SELECT * from item where id = {}".format(item_id)
    item_ = select_query(query)[0]
    query = "SELECT phone from user where mail = '{}'".format(item_.get('owners_mail'))
    phone_as_int = select_query(query)[0].get('phone')
    phone_str = "0" + str(phone_as_int)
    item_["phone"] = phone_str
    return item_

def get_size_item():
    query = "SELECT COUNT(*) FROM item"
    print(query,type(query),select_query(query)[0]["COUNT(*)"])
    return  int(select_query(query)[0]["COUNT(*)"])

