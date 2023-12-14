from sql_base.models import LoginM 
from sql_base.base import base_worker

def check_login_request(user: LoginM):
    user = base_worker.insert_data(f"SELECT * FROM user WHERE login = ? AND password = ?",(user.login,user.password))
    return user