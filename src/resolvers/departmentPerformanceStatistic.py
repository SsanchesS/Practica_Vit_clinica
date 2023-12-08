from sql_base.base import base_worker
from sql_base.models import departmentPerformanceStatisticsM as dPSM

def get_dPS(applicationExecutor_id) -> int:
    get_dPS1 = base_worker.insert_data(f"SELECT * FROM departmentPerformanceStatistics WHERE applicationExecutor_id = {applicationExecutor_id}",())
    return get_dPS1

def new_dPS(dPS: dPSM) -> int:
    new_id = base_worker.insert_data(f"""
        INSERT INTO departmentPerformanceStatistics (NumberCompletedApplications, AvgApplicationTime, statisticsTypesDiseases) 
        VALUES (?, ?, ?) RETURNING applicationExecutor_id;
    """, (dPS.NumberCompletedApplications, dPS.AvgApplicationTime, dPS.statisticsTypesDiseases))
    return new_id

def upd_dPS(applicationExecutor_id, dPS: dPSM) -> int:
    upd_id = base_worker.insert_data(f"""
        UPDATE departmentPerformanceStatistics 
        SET NumberCompletedApplications = ?, AvgApplicationTime = ?, statisticsTypesDiseases = ?
        WHERE applicationExecutor_id = {applicationExecutor_id} 
        RETURNING applicationExecutor_id;
    """, (dPS.NumberCompletedApplications, dPS.AvgApplicationTime, dPS.statisticsTypesDiseases))
    return upd_id

def del_dPS(applicationExecutor_id) -> int:
    del_id = base_worker.insert_data(f"DELETE FROM departmentPerformanceStatistics WHERE applicationExecutor_id = {applicationExecutor_id} RETURNING applicationExecutor_id;",())
    return del_id