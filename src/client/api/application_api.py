import requests
from tkinter import *

def create_application_app(root,font):
   application_app = Toplevel(root)
   application_app.title("Работа с application")  
   application_app.geometry('1400x900')

   get_id = StringVar()
   upd_id = StringVar()
   del_id = StringVar()

   new_application_dataAt = StringVar()
   upd_application_dataAt = StringVar()

   new_application_animal = StringVar()
   upd_application_animal = StringVar()

   new_application_treatmentType = StringVar()
   upd_application_treatmentType = StringVar()

   new_application_descriptionDisease = StringVar()
   upd_application_descriptionDisease = StringVar()

   new_application_customerData = StringVar()
   upd_application_customerData = StringVar()

   new_application_treatmentStatus = StringVar()
   upd_application_treatmentStatus = StringVar()


#

   lbl_get_application = Label(application_app, text="Показать application по id", font=font)
   entry_get_application = Entry(application_app, font=font, textvariable=get_id)
   btn_get_application = Button(application_app, text='Получить', font=font, command=lambda: fun_get_application(entry_get_application.get()))
   lbl_get_application.grid(row=1, column=1)
   entry_get_application.grid(row=2, column=0)
   btn_get_application.grid(row=2, column=1)

#

   lbl_new_application = Label(application_app, text='Добавить нового application', font=font)

   lbl_new_application_dataAt = Label(application_app, text='Введите dataAt нового application', font=font)
   entry_new_application_dataAt_data = Entry(application_app, font=font, textvariable=new_application_dataAt)

   lbl_new_application_animal = Label(application_app, text='Введите animal нового application', font=font)
   entry_new_application_animal_data = Entry(application_app, font=font, textvariable=new_application_animal)

   lbl_new_application_treatmentType = Label(application_app, text='Введите treatmentType нового application', font=font)
   entry_new_application_treatmentType_data = Entry(application_app, font=font, textvariable=new_application_treatmentType)

   lbl_new_application_descriptionDisease = Label(application_app, text='Введите descriptionDisease нового application', font=font)
   entry_new_application_descriptionDisease_data = Entry(application_app, font=font, textvariable=new_application_descriptionDisease)

   lbl_new_application_customerData = Label(application_app, text='Введите customerData нового application', font=font)
   entry_new_application_customerData_data = Entry(application_app, font=font, textvariable=new_application_customerData)

   lbl_new_application_treatmentStatus = Label(application_app, text='Введите treatmentStatus нового application', font=font)
   entry_new_application_treatmentStatus_data = Entry(application_app, font=font, textvariable=new_application_treatmentStatus)
#

   btn_new_application = Button(application_app, text='Создать', font=font, command=lambda: fun_new_application(entry_new_application_dataAt_data.get(),entry_new_application_animal_data.get(),entry_new_application_treatmentType_data.get(),entry_new_application_descriptionDisease_data.get(),entry_new_application_customerData_data.get(),entry_new_application_treatmentStatus_data.get()))
   lbl_new_application.grid(row=3, column=1)

   lbl_new_application_dataAt.grid(row=4, column=0)
   entry_new_application_dataAt_data.grid(row=4, column=2)

   lbl_new_application_animal.grid(row=5, column=0)
   entry_new_application_animal_data.grid(row=5, column=2)

   lbl_new_application_treatmentType.grid(row=6, column=0)
   entry_new_application_treatmentType_data.grid(row=6, column=2)

   lbl_new_application_descriptionDisease.grid(row=7, column=0)
   entry_new_application_descriptionDisease_data.grid(row=7, column=2)

   lbl_new_application_customerData.grid(row=8, column=0)
   entry_new_application_customerData_data.grid(row=8, column=2)

   lbl_new_application_treatmentStatus.grid(row=9, column=0)
   entry_new_application_treatmentStatus_data.grid(row=9, column=2)

   btn_new_application.grid(row=10, column=1)

#

   lbl_upd_application = Label(application_app, text='Обновить application по id', font=font)

   lbl_upd_application_id = Label(application_app, text='Введите application_id', font=font)
   entry_upd_application = Entry(application_app, font=font, textvariable=upd_id)

   lbl_upd_application_dataAt = Label(application_app, text='Введите dataAt application', font=font)
   entry_upd_application_dataAt_data = Entry(application_app, font=font, textvariable=upd_application_dataAt)

   lbl_upd_application_animal = Label(application_app, text='Введите animal application', font=font)
   entry_upd_application_animal_data = Entry(application_app, font=font, textvariable=upd_application_animal)

   lbl_upd_application_treatmentType = Label(application_app, text='Введите treatmentType application', font=font)
   entry_upd_application_treatmentType_data = Entry(application_app, font=font, textvariable=upd_application_treatmentType)

   lbl_upd_application_descriptionDisease = Label(application_app, text='Введите descriptionDisease application', font=font)
   entry_upd_application_descriptionDisease_data = Entry(application_app, font=font, textvariable=upd_application_descriptionDisease)

   lbl_upd_application_customerData = Label(application_app, text='Введите customerData application', font=font)
   entry_upd_application_customerData_data = Entry(application_app, font=font, textvariable=upd_application_customerData)

   lbl_upd_application_treatmentStatus = Label(application_app, text='Введите treatmentStatus application', font=font)
   entry_upd_application_treatmentStatus_data = Entry(application_app, font=font, textvariable=upd_application_treatmentStatus)
#

   btn_upd_application = Button(application_app, text='Обновить', font=font, command=lambda: fun_upd_application(entry_upd_application.get(),entry_upd_application_dataAt_data.get(),entry_upd_application_animal_data.get(),entry_upd_application_treatmentType_data.get(),entry_upd_application_descriptionDisease_data.get(),entry_upd_application_customerData_data.get(),entry_upd_application_treatmentStatus_data.get()))

   lbl_upd_application.grid(row=11, column=1)

   lbl_upd_application_id.grid(row=12, column=0)
   entry_upd_application.grid(row=12, column=2)

   lbl_upd_application_dataAt.grid(row=13, column=0)
   entry_upd_application_dataAt_data.grid(row=13, column=2)

   lbl_upd_application_animal.grid(row=14, column=0)
   entry_upd_application_animal_data.grid(row=14, column=2)

   lbl_upd_application_treatmentType.grid(row=15, column=0)
   entry_upd_application_treatmentType_data.grid(row=15, column=2)

   lbl_upd_application_descriptionDisease.grid(row=16, column=0)
   entry_upd_application_descriptionDisease_data.grid(row=16, column=2)

   lbl_upd_application_customerData.grid(row=17, column=0)
   entry_upd_application_customerData_data.grid(row=17, column=2)

   lbl_upd_application_treatmentStatus.grid(row=18, column=0)
   entry_upd_application_treatmentStatus_data.grid(row=18, column=2)

   btn_upd_application.grid(row=19, column=1)

#

   lbl_del_application = Label(application_app, text='Удалить application по id', font=font)
   entry_del_application = Entry(application_app, font=font, textvariable=del_id)
   btn_del_application = Button(application_app, text='Удалить', font=font, command=lambda: fun_del_application(entry_del_application.get()))

   lbl_del_application.grid(row=20, column=1)
   entry_del_application.grid(row=21, column=0)
   btn_del_application.grid(row=21, column=1)


#
   global lb2_response
   lb1_response = Label(application_app, text='Полученный ответ', font=font)
   lb2_response = Label(application_app, text='', font=font)

   lb1_response.grid(row=22, column=1)
   lb2_response.grid(row=23, column=1)

#

   lbl_get_applications = Label(application_app, text="Показать applications", font=font)
   btn_get_applications = Button(application_app, text='Получить', font=font, command=lambda: fun_get_applications())
   lbl_get_applications.grid(row=24, column=0)
   btn_get_applications.grid(row=24, column=1)

#

def get_response(s):
   response = s
   print(response)
   lb2_response.config(text=response)

#
def fun_get_applications():
   r = requests.get(f'http://127.0.0.1:8000/application/')
   answer = r.json()
   get_response(answer)

def fun_get_application(application_id):
   r = requests.get(f'http://127.0.0.1:8000/application/{application_id}')
   answer = r.json()
   get_response(answer)

def fun_new_application(dataAt,animal,treatmentType,descriptionDisease,customerData,treatmentStatus):
   data = f'{{ "dataAt": "{dataAt}", "animal": "{animal}", "treatmentType": "{treatmentType}", "descriptionDisease": "{descriptionDisease}", "customerData": "{customerData}", "treatmentStatus": "{treatmentStatus}"}}'
   r = requests.post(f'http://127.0.0.1:8000/application/',data=data)
   answer = r.json()
   get_response(answer)

def fun_upd_application(application_id,dataAt,animal,treatmentType,descriptionDisease,customerData,treatmentStatus):
   data = f'{{ "dataAt": "{dataAt}", "animal": "{animal}", "treatmentType": "{treatmentType}", "descriptionDisease": "{descriptionDisease}", "customerData": "{customerData}", "treatmentStatus": "{treatmentStatus}"}}'
   r = requests.put(f'http://127.0.0.1:8000/application/{application_id}',data=data)
   answer = r.json()
   get_response(answer)

def fun_del_application(application_id):
   r = requests.delete(f'http://127.0.0.1:8000/application/{application_id}')
   answer = r.json()
   get_response(answer)