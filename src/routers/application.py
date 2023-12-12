from fastapi import APIRouter
from sql_base.models import applicationM
import resolvers.application

application_router = APIRouter()

@application_router.get('/')
def get_applications():
    applications = resolvers.application.get_applications()
    if applications is None:
        return {"code": 404, 'message': f"applications not found"}
    return {"code": 201, "applications": applications}

@application_router.get('/{application_id}')
def get_application(application_id: int):
    application = resolvers.application.get_application(application_id)
    if application is None:
        return {"code": 404, 'message': f"application with id {application_id} not found"}
    return {"code": 201, "application": application}

@application_router.post('/')
def new_application(application: applicationM):
    new_id = resolvers.application.new_application(application)
    return {"code": 201, "id": new_id}

@application_router.put('/{application_id}')
def update_application(application_id: int, application: applicationM):
    upd_id = resolvers.application.upd_application(application_id, application)
    if upd_id is None:
        return {"code": 404, 'message': f"application with id {application_id} not found"}
    return {"code": 201, "Update application": upd_id}

# @application_router.put('/{application_id}')
# def update_private_application(application_id: int, application: applicationM):
#     upd_id = resolvers.application.upd_private_application(application_id, application)
#     if upd_id is None:
#         return {"code": 404, 'message': f"application with id {application_id} not found"}
#     return {"code": 201, "Update application": upd_id}

@application_router.delete('/{application_id}')
def delete_application(application_id: int):
    del_id = resolvers.application.del_application(application_id)
    if del_id is None:
        return {"code": 404, 'message': f"application with id {application_id} not found"}
    return {"code": 201, "Delete application": del_id}