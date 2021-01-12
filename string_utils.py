import re 
from models import community
def is_valid_email(mail_str):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if(re.search(regex,mail_str)):  
        return True  
    else:  
        return False

def is_valid_phone(phone_num):
    pattern = r'05[0-9]{8}' 
    compile_obj = re.compile(pattern)
    if(compile_obj.search(phone_num)):  
        return True  
    else:  
        return False
community.insert("a","1", "aa@gmail.com", None)