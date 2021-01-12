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

def get_community_id_of_user(user_email):
    community_query = '''SELECT community_id 
                FROM user
                WHERE mail = '{}' '''.format(user_email)
    res_comm = select_query(community_query)
    community_id = res_comm[0].get('community_id')
    return community_id

def get_item_by_email(user_email):
    community_id = get_community_id_of_user(user_email)

    items_query = '''SELECT i.name as name, i.id as id , i.img_path as img_path, i.description as description
                FROM user as u JOIN item as i ON i.owners_mail = u.mail
                WHERE mail <> '{}' and u.community_id = {} and i.is_available = 1'''.format(user_email, community_id)  
    res_items = select_query(items_query) 
    return res_items

