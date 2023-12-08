from fastapi import APIRouter
from sql_base.models import userM
import resolvers.user

user_router = APIRouter()

@user_router.get('/{user_id}')
def get_user(user_id: int):
    user = resolvers.user.get_user(user_id)
    if user is None:
        return {"code": 404, 'message': f"user with id {user_id} not found"}
    return {"code": 201, 'user': user}

@user_router.post('/')
def new_user(user: userM):
    new_id = resolvers.user.new_user(user)
    return {"code": 201, "id": new_id}

@user_router.put('/{user_id}')
def update_user(user_id: int, user: userM):
    upd_id = resolvers.user.upd_user(user_id, user)
    if upd_id is None:
        return {"code": 404, 'message': f"user with id {user_id} not found"}
    return {"code": 201, "Update user": upd_id}

@user_router.delete('/{user_id}')
def delete_user(user_id: int):
    del_id = resolvers.user.del_user(user_id)
    if del_id is None:
        return {"code": 404, 'message': f"user with id {user_id} not found"}
    return {"code": 201, "Delete user": del_id}