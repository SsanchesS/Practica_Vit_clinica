from sql_base.models import LoginM 
from sql_base.base import base_worker

def check_login_request(user: LoginM):
    user_id = base_worker.insert_data(f"SELECT user_id FROM user WHERE login = ? AND password = ?",(user.login,user.password))
    return user_id