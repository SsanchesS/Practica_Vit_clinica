import requests
from tkinter import *

def create_applicationPrivate_app(root,font):
   applicationPrivate_app = Toplevel(root)
   applicationPrivate_app.title("Работа с applicationPrivate")  
   applicationPrivate_app.geometry('1400x700')

   get_id = StringVar()
   upd_id = StringVar()

   upd_applicationPrivate_treatmentStage = StringVar()

   upd_applicationPrivate_descriptionTreatment = StringVar()

   upd_applicationPrivate_veterinarian_id = StringVar()

   upd_applicationPrivate_applicationStatus = StringVar()

   upd_applicationPrivate_applicationExecutor = StringVar()

   upd_applicationPrivate_comments = StringVar()


#

   lbl_get_applicationPrivate = Label(applicationPrivate_app, text="Показать application по id", font=font)
   entry_get_applicationPrivate = Entry(applicationPrivate_app, font=font, textvariable=get_id)
   btn_get_applicationPrivate = Button(applicationPrivate_app, text='Получить', font=font, command=lambda: fun_get_applicationPrivate(entry_get_applicationPrivate.get()))
   lbl_get_applicationPrivate.grid(row=1, column=1)
   entry_get_applicationPrivate.grid(row=2, column=0)
   btn_get_applicationPrivate.grid(row=2, column=1)

#

   lbl_upd_applicationPrivate = Label(applicationPrivate_app, text='Обновить applicationPrivate по id', font=font)

   lbl_upd_applicationPrivate_id = Label(applicationPrivate_app, text='Введите applicationPrivate_id', font=font)
   entry_upd_applicationPrivate = Entry(applicationPrivate_app, font=font, textvariable=upd_id)

   lbl_upd_applicationPrivate_treatmentStage = Label(applicationPrivate_app, text='Введите treatmentStage applicationPrivate', font=font)
   entry_upd_applicationPrivate_treatmentStage_data = Entry(applicationPrivate_app, font=font, textvariable=upd_applicationPrivate_treatmentStage)

   lbl_upd_applicationPrivate_descriptionTreatment = Label(applicationPrivate_app, text='Введите descriptionTreatment applicationPrivate', font=font)
   entry_upd_applicationPrivate_descriptionTreatment_data = Entry(applicationPrivate_app, font=font, textvariable=upd_applicationPrivate_descriptionTreatment)

   lbl_upd_applicationPrivate_veterinarian_id = Label(applicationPrivate_app, text='Введите veterinarian_id applicationPrivate', font=font)
   entry_upd_applicationPrivate_veterinarian_id_data = Entry(applicationPrivate_app, font=font, textvariable=upd_applicationPrivate_veterinarian_id)

   lbl_upd_applicationPrivate_applicationStatus = Label(applicationPrivate_app, text='Введите applicationStatus applicationPrivate', font=font)
   entry_upd_applicationPrivate_applicationStatus_data = Entry(applicationPrivate_app, font=font, textvariable=upd_applicationPrivate_applicationStatus)

   lbl_upd_applicationPrivate_applicationExecutor = Label(applicationPrivate_app, text='Введите applicationPrivate_applicationExecutor', font=font)
   entry_upd_applicationPrivate_applicationExecutor_data = Entry(applicationPrivate_app, font=font, textvariable=upd_applicationPrivate_applicationExecutor)

   lbl_upd_applicationPrivate_comments = Label(applicationPrivate_app, text='Введите applicationPrivate_comments', font=font)
   entry_upd_applicationPrivate_comments_data = Entry(applicationPrivate_app, font=font, textvariable=upd_applicationPrivate_comments)

#

   btn_upd_applicationPrivate = Button(applicationPrivate_app, text='Обновить', font=font, command=lambda: fun_upd_applicationPrivate(entry_upd_applicationPrivate.get(),entry_upd_applicationPrivate_treatmentStage_data.get(),entry_upd_applicationPrivate_descriptionTreatment_data.get(),entry_upd_applicationPrivate_veterinarian_id_data.get(),entry_upd_applicationPrivate_applicationStatus_data.get(),entry_upd_applicationPrivate_applicationExecutor_data.get(),entry_upd_applicationPrivate_comments_data.get()))
   lbl_upd_applicationPrivate.grid(row=3, column=1)

   lbl_upd_applicationPrivate_id.grid(row=4, column=0)
   entry_upd_applicationPrivate.grid(row=4, column=2)

   lbl_upd_applicationPrivate_treatmentStage.grid(row=5, column=0)
   entry_upd_applicationPrivate_treatmentStage_data.grid(row=5, column=2)

   lbl_upd_applicationPrivate_descriptionTreatment.grid(row=6, column=0)
   entry_upd_applicationPrivate_descriptionTreatment_data.grid(row=6, column=2)

   lbl_upd_applicationPrivate_veterinarian_id.grid(row=7, column=0)
   entry_upd_applicationPrivate_veterinarian_id_data.grid(row=7, column=2)

   lbl_upd_applicationPrivate_applicationStatus.grid(row=8, column=0)
   entry_upd_applicationPrivate_applicationStatus_data.grid(row=8, column=2)

   lbl_upd_applicationPrivate_applicationExecutor.grid(row=9, column=0)
   entry_upd_applicationPrivate_applicationExecutor_data.grid(row=9, column=2)

   lbl_upd_applicationPrivate_comments.grid(row=10, column=0)
   entry_upd_applicationPrivate_comments_data.grid(row=10, column=2)

   btn_upd_applicationPrivate.grid(row=11, column=1)

#
   global lb2_response
   lb1_response = Label(applicationPrivate_app, text='Полученный ответ', font=font)
   lb2_response = Label(applicationPrivate_app, text='', font=font)

   lb1_response.grid(row=12, column=1)
   lb2_response.grid(row=13, column=1)

def get_response(s):
   response = s
   print(response)
   lb2_response.config(text=response)

#

def fun_get_applicationPrivate(applicationPrivate_id):
   r = requests.get(f'http://127.0.0.1:8000/applicationPrivate/{applicationPrivate_id}')
   answer = r.json()
   get_response(answer)

def fun_upd_applicationPrivate(applicationPrivate_id,treatmentStage,descriptionTreatment,veterinarian_id,applicationStatus,applicationExecutor,comments):
   data = f'{{ "treatmentStage": "{treatmentStage}", "descriptionTreatment": "{descriptionTreatment}", "veterinarian_id": "{veterinarian_id}", "applicationStatus": "{applicationStatus}", "applicationExecutor": "{applicationExecutor}", "comments": "{comments}" }}'
   r = requests.put(f'http://127.0.0.1:8000/applicationPrivate/{applicationPrivate_id}',data=data)
   answer = r.json()
   get_response(answer)