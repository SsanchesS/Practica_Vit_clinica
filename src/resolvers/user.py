from sql_base.base import base_worker
from sql_base.models import userM

def get_user(user_id) -> str:
    get_user = base_worker.insert_data(f"SELECT * FROM user WHERE user_id = {user_id}",())
    return get_user

def new_user(user: userM) -> str:
    new_user_id = base_worker.insert_data(f"""
        INSERT INTO user (name, login, password, role_id) 
        VALUES (?, ?, ?, ?) RETURNING user_id;
    """, (user.name, user.login, user.password, user.role_id))
    return new_user_id

def upd_user(user_id, user: userM) -> str:
    upd_user_id = base_worker.insert_data(f"""
        UPDATE user 
        SET name = ?, login = ?, password = ?, role_id = ?
        WHERE user_id = {user_id} 
        RETURNING user_id;
    """, (user.name, user.login, user.password, user.role_id))
    return upd_user_id

def del_user(user_id) -> str:
    del_user_id = base_worker.insert_data(f"DELETE FROM user WHERE user_id = {user_id} RETURNING user_id;",())
    return del_user_id