from fastapi import APIRouter
from sql_base.models import applicationM
import resolvers.application

applicationPrivate_router = APIRouter()

@applicationPrivate_router.get('/{application_id}')
def get_application(application_id: int):
    application = resolvers.application.get_application(application_id)
    if application is None:
        return {"code": 404, 'message': f"application with id {application_id} not found"}
    return {"code": 201, "application": application}

@applicationPrivate_router.put('/{application_id}')
def update_private_application(application_id: int, application: applicationM):
    upd_id = resolvers.application.upd_private_application(application_id, application)
    if upd_id is None:
        return {"code": 404, 'message': f"application with id {application_id} not found"}
    return {"code": 201, "Update application": upd_id}
