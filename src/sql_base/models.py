from typing import Optional
from pydantic import BaseModel
from datetime import date

class applicationM(BaseModel): # Заявка
    # application_id: int
    dataAt: str  = None
    animal: str  = None
    treatmentType: str  = None # Тип лечения
    descriptionDisease : str  = None # Описание заболевания
    customerData: str  = None
    treatmentStatus : str  = None # Статус лечения
    
    # private

    treatmentStage : Optional[str] = None # Этап лечения 
    descriptionTreatment: Optional[str] = None
    veterinarian_id : Optional[int] = None

    applicationStatus : Optional[str] = None

    applicationExecutor : Optional[int] = None # исполнитель заявки
    comments: Optional[str] = None

class veterinarianM(BaseModel):
    # veterinarian_id: int
    name: str
 
class departmentPerformanceStatisticsM(BaseModel): # Статистика работы отдела
    # applicationExecutor_id: int
    NumberCompletedApplications: int # Количество выполненных заявок
    AvgApplicationTime: int # Среднее время выполнения заявки
    statisticsTypesDiseases: str # Статистика по типам заболеваний

class LoginM(BaseModel):
    login: str
    password: str 

class roleM(BaseModel):
    # role_id: int
    role: str #private

class userM(BaseModel):
    # user_id: int
    name:str
    login: str
    password: str
    role_id:int #private