from typing import Optional
from pydantic import BaseModel
from datetime import date

class applicationM(BaseModel): # Заявка
    # application_id: int
    dataAt: date
    animal: str
    treatmentType: str # Тип лечения
    descriptionDisease : str # Описание заболевания
    customerData: str
    treatmentStatus : str # Статус лечения
    
    # private

    treatmentStage : Optional[str] # Этап лечения 
    descriptionTreatment: Optional[str]
    veterinarian_id : Optional[int]

    applicationStatus : Optional[str]

    applicationExecutor : Optional[int] # исполнитель заявки
    comments: Optional[str]

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