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

# не тестил
def upd_private_application(application_id, application: applicationM) -> int:
    print("Prinyal")
    set_clauses = []
    values = []

    def f2(obj):
        return obj + '=?,'
    
    if(application.treatmentStage):
        set_clauses.append('treatment_stage')
        values.append(application.treatmentStage)

    if(application.descriptionTreatment):
        set_clauses.append('description_treatment')
        values.append(application.descriptionTreatment)

    if(application.veterinarian_id):
        set_clauses.append('veterinarian_id')
        values.append(application.veterinarian_id)

    if(application.applicationStatus):
        set_clauses.append('application_status')
        values.append(application.applicationStatus)

    if(application.applicationExecutor):
        set_clauses.append('application_executor')
        values.append(application.applicationExecutor)

    if(application.comments):
        set_clauses.append('comments')
        values.append(application.comments)

    set_clause = ', '.join(map(f2, set_clauses))
    set_clause = set_clause.rstrip(',')  # Убираем последнюю запятую

    upd_id = base_worker.insert_data(f"""
        UPDATE application
        SET {set_clause}
        WHERE application_id = {application_id} 
        RETURNING application_id;
    """, (values))
    return upd_id

def del_application(application_id) -> int:
    del_id = base_worker.insert_data(f"DELETE FROM application WHERE application_id = {application_id} RETURNING application_id;",())
    return del_id