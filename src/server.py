from fastapi import FastAPI
import uvicorn

from routers.application import application_router
from routers.applicationPrivate import applicationPrivate_router
from routers.veterinarian import veterinarian_router
from routers.departmentPerformanceStatistic import dPS_router
from routers.user import user_router

from routers.login import login_router

from sql_base.base import base_worker


BASE_PATH = 'Vit_clinic.db'
base_worker.set_base_path(BASE_PATH)

if not base_worker.check_base():
    print("БД не существует")
    base_worker.create_base('../sql/base.sql')
else:
    print("БД существует")
    

app = FastAPI()

@app.get("/")
def main_page():
    return {'page': 'Connection in correct'}
    
app.include_router(application_router, prefix='/application')
app.include_router(applicationPrivate_router, prefix='/applicationPrivate')
app.include_router(veterinarian_router, prefix='/veterinarian')
app.include_router(dPS_router, prefix='/dPS')
app.include_router(user_router, prefix='/user')

app.include_router(login_router, prefix='/login')

if __name__ == "__main__":
    uvicorn.run("server:app", port=8000, host="127.0.0.1", reload=True)