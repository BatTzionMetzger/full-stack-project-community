from models.db_queries import *
# from db_queries import *

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


def check_if_user_exists_by_email_and_password(email, password):
    query = '''SELECT count(*) FROM user 
        WHERE mail = '{}' and password = {}'''.format(email, password)
    res = select_query(query)
    if res[0].get('count(*)') > 0:
        return True
    return False

def get_user_ownered_products(user_email):
    items_query = '''SELECT *
                FROM  item 
                WHERE owners_mail = '{}' and  is_available = 1'''.format(user_email)  
    res_items = select_query(items_query) 
    return res_items

def get_all_user_in_communitiy_of_user(user_email):
    community_id = get_community_id_of_user(user_email)
    users_query = '''SELECT name ,  mail 
                FROM user 
                WHERE mail <> '{}' and community_id = {} '''.format(user_email, community_id)  
    res_users = select_query(users_query) 
    return res_users

def get_owner_email(user_email):
    community_id = get_community_id_of_user(user_email)
    admin_mail_query = '''SELECT admin_mail 
                FROM community 
                WHERE id = {} '''.format(community_id)  
    res_admin_mail = select_query(admin_mail_query) 
    return res_admin_mail[0].get('admin_mail')
