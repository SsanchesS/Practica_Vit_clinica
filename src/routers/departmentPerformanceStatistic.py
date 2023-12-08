from fastapi import APIRouter
from sql_base.models import departmentPerformanceStatisticsM as dPSM
import resolvers.departmentPerformanceStatistic

dPS_router = APIRouter()

@dPS_router.get('/{dPS_id}')
def get_dPS(dPS_id: int):
    dPS = resolvers.departmentPerformanceStatistic.get_dPS(dPS_id)
    if dPS is None:
        return {"code": 404, 'message': f"dPS with id {dPS_id} not found"}
    return {"code": 201, "dPS": dPS}

@dPS_router.post('/')
def new_dPS(dPS: dPSM):
    new_id = resolvers.departmentPerformanceStatistic.new_dPS(dPS)
    return {"code": 201, "id": new_id}

@dPS_router.put('/{dPS_id}')
def update_dPS(dPS_id: int, dPS: dPSM):
    upd_id = resolvers.departmentPerformanceStatistic.upd_dPS(dPS_id, dPS)
    if upd_id is None:
        return {"code": 404, 'message': f"dPS with id {dPS_id} not found"}
    return {"code": 201, "Update dPS": upd_id}

@dPS_router.delete('/{dPS_id}')
def delete_dPS(dPS_id: int):
    del_id = resolvers.departmentPerformanceStatistic.del_dPS(dPS_id)
    if del_id is None:
        return {"code": 404, 'message': f"dPS with id {dPS_id} not found"}
    return {"code": 201, "Delete dPS": del_id}