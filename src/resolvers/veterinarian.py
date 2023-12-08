from sql_base.base import base_worker
from sql_base.models import veterinarianM

def get_veterinarian(veterinarian_id) -> int:
    get_veterinarian = base_worker.insert_data(f"SELECT * FROM veterinarian WHERE veterinarian_id = {veterinarian_id}",())
    return get_veterinarian

def new_veterinarian(veterinarian: veterinarianM) -> int:
    new_id = base_worker.insert_data(f"""
        INSERT INTO veterinarian (name) 
        VALUES (?) RETURNING veterinarian_id;
    """, (veterinarian.name))
    return new_id

def upd_veterinarian(veterinarian_id, veterinarian: veterinarianM) -> int:
    upd_id = base_worker.insert_data(f"""
        UPDATE veterinarian 
        SET name = ?
        WHERE veterinarian_id = {veterinarian_id} 
        RETURNING veterinarian_id;
    """, (veterinarian.name))
    return upd_id

def del_veterinarian(veterinarian_id) -> int:
    del_id = base_worker.insert_data(f"DELETE FROM veterinarian WHERE veterinarian_id = {veterinarian_id} RETURNING veterinarian_id;",())
    return del_id