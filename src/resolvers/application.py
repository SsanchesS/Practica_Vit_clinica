from sql_base.base import base_worker
from sql_base.models import applicationM

def get_applications():
    get_applications = base_worker.insert_data(f"SELECT * FROM application",())
    return get_applications

def get_application(application_id):
    get_application = base_worker.insert_data(f"SELECT * FROM application WHERE application_id = {application_id}",())
    return get_application

def new_application(application: applicationM) -> int:
    new_id = base_worker.insert_data(f"""
        INSERT INTO application (dataAt, animal, treatmentType, descriptionDisease, customerData, treatmentStatus)
        VALUES (?, ?, ?, ?, ?, ?) RETURNING application_id;
    """, (application.dataAt, application.animal, application.treatmentType, application.descriptionDisease, application.customerData, application.treatmentStatus))
    return new_id
# 
def upd_application(application_id, application: applicationM) -> int:
    upd_id = base_worker.insert_data(f"""
        UPDATE application
        SET dataAt = ?, animal = ?, treatmentType = ?, descriptionDisease = ?, customerData = ?, treatmentStatus = ?
        WHERE application_id = {application_id} 
        RETURNING application_id;
    """, (application.dataAt, application.animal, application.treatmentType, application.descriptionDisease, application.customerData, application.treatmentStatus))
    return upd_id

def upd_private_application(application_id, application: applicationM) -> int:
    upd_id = base_worker.insert_data(f"""
        UPDATE application
        SET treatmentStage=?,descriptionTreatment=?,veterinarian_id=?,applicationStatus=?,applicationExecutor_id=?,comments=?
        WHERE application_id = {application_id} 
        RETURNING application_id;
    """, (application.treatmentStage,application.descriptionTreatment,application.veterinarian_id,application.applicationStatus,application.applicationExecutor_id,application.comments))
    return upd_id

def del_application(application_id) -> int:
    del_id = base_worker.insert_data(f"DELETE FROM application WHERE application_id = {application_id} RETURNING application_id;",())
    return del_id