from fastapi import APIRouter
from sql_base.models import LoginM
from resolvers.check_login import check_login_request

login_router = APIRouter()

@login_router.post('/')
def check_login_response(user:LoginM):
    user = check_login_request(user)
    user_id = user[0]
    role_id = user[4]
    if user_id:
        return {"code": 200, "message": "Login correct", 'user_id': user_id,'role_id':role_id}
    else:
        return {"code": 401, "message": "Login incorrect, try again"}