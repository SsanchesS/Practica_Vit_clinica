from sql_base.base import base_worker
from sql_base.models import applicationM

def get_applications():
    get_applications = base_worker.insert_data(f"SELECT * FROM application",())
    return get_applications

def get_application(application_id):
    get_application = base_worker.insert_data(f"SELECT * FROM application WHERE application_id = {application_id}",())
    return get_application

def new_application(application: applicationM) -> int:

    insert_fields = []
    insert_values = []

    if application.dataAt is not None:
        insert_fields.append("dataAt")
        insert_values.append(f"'{application.dataAt}'")

    if application.animal is not None:
        insert_fields.append("animal")
        insert_values.append(f"'{application.animal}'")

    if application.treatmentType is not None:
        insert_fields.append("treatmentType")
        insert_values.append(f"'{application.treatmentType}'")

    if application.descriptionDisease is not None:
        insert_fields.append("descriptionDisease")
        insert_values.append(f"'{application.descriptionDisease}'")

    if application.customerData is not None:
        insert_fields.append("customerData")
        insert_values.append(f"'{application.customerData}'")

    if application.treatmentStatus is not None:
        insert_fields.append("treatmentStatus")
        insert_values.append(f"'{application.treatmentStatus}'")

    fields_str = ', '.join(insert_fields)
    values_str = ', '.join(insert_values)

    new_id = base_worker.insert_data(f"""
        INSERT INTO application ({fields_str})
        VALUES ({values_str})
        RETURNING application_id;
    """, ())
    
    return new_id

# 

def upd_application(application_id, application: applicationM) -> int:

    update_fields = []

    if application.dataAt is not None and application.dataAt != '':
        update_fields.append(f"dataAt = '{application.dataAt}'")

    if application.animal is not None and application.animal != '':
        update_fields.append(f"animal = '{application.animal}'")

    if application.treatmentType is not None and application.treatmentType != '':
        update_fields.append(f"treatmentType = '{application.treatmentType}'")

    if application.descriptionDisease is not None and application.descriptionDisease != '':
        update_fields.append(f"descriptionDisease = '{application.descriptionDisease}'")

    if application.customerData is not None and application.customerData != '':
        update_fields.append(f"customerData = '{application.customerData}'")

    if application.treatmentStatus is not None and application.treatmentStatus != '':
        update_fields.append(f"treatmentStatus = '{application.treatmentStatus}'")

    update_fields_str = ', '.join(update_fields)

    upd_id = base_worker.insert_data(f"""
        UPDATE application
        SET {update_fields_str}
        WHERE application_id = {application_id} 
        RETURNING application_id;
    """, ())

    return upd_id

def upd_private_application(application_id, application: applicationM) -> int:

    update_fields = []

    if application.treatmentStage is not None:
        update_fields.append(f"treatmentStage = '{application.treatmentStage}'")

    if application.descriptionTreatment is not None:
        update_fields.append(f"descriptionTreatment = '{application.descriptionTreatment}'")

    if application.veterinarian_id is not None:
        update_fields.append(f"veterinarian_id = {application.veterinarian_id}")

    if application.applicationStatus is not None:
        update_fields.append(f"applicationStatus = '{application.applicationStatus}'")

    if application.applicationExecutor_id is not None:
        update_fields.append(f"applicationExecutor_id = {application.applicationExecutor_id}")

    if application.comments is not None:
        update_fields.append(f"comments = '{application.comments}'")

    update_fields_str = ', '.join(update_fields)

    upd_id = base_worker.insert_data(f"""
        UPDATE application
        SET {update_fields_str}
        WHERE application_id = {application_id} 
        RETURNING application_id;
    """, ())

    return upd_id

def del_application(application_id) -> int:
    del_id = base_worker.insert_data(f"DELETE FROM application WHERE application_id = {application_id} RETURNING application_id;", ())
    return del_id