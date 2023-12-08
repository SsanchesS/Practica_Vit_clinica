from fastapi import APIRouter
from sql_base.models import veterinarianM
import resolvers.veterinarian

veterinarian_router = APIRouter()

@veterinarian_router.get('/{veterinarian_id}')
def get_veterinarian(veterinarian_id: int):
    veterinarian = resolvers.veterinarian.get_veterinarian(veterinarian_id)
    if veterinarian is None:
        return {"code": 404, 'message': f"veterinarian with id {veterinarian_id} not found"}
    return {"code": 201, "veterinarian": veterinarian}

@veterinarian_router.post('/')
def new_veterinarian(veterinarian: veterinarianM):
    new_id = resolvers.veterinarian.new_veterinarian(veterinarian)
    return {"code": 201, "id": new_id}

@veterinarian_router.put('/{veterinarian_id}')
def update_veterinarian(veterinarian_id: int, veterinarian: veterinarianM):
    upd_id = resolvers.veterinarian.upd_veterinarian(veterinarian_id, veterinarian)
    if upd_id is None:
        return {"code": 404, 'message': f"veterinarian with id {veterinarian_id} not found"}
    return {"code": 201, "Update veterinarian": upd_id}
    
@veterinarian_router.delete('/{veterinarian_id}')
def delete_veterinarian(veterinarian_id: int):
    del_id = resolvers.veterinarian.del_veterinarian(veterinarian_id)
    if del_id is None:
        return {"code": 404, 'message': f"veterinarian with id {veterinarian_id} not found"}
    return {"code": 201, "Delete veterinarian": del_id}