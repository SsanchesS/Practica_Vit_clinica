import requests
from tkinter import *

def create_dPS_app(root,font):
   dPS_app = Toplevel(root)
   dPS_app.title("Работа со статистикой работы отдела")  
   dPS_app.geometry('1400x700')


   get_id = StringVar()
   upd_id = StringVar()
   del_id = StringVar()

   new_dPS_NumberCompletedApplications = StringVar()
   upd_dPS_NumberCompletedApplications = StringVar()

   new_dPS_AvgApplicationTime = StringVar()
   upd_dPS_AvgApplicationTime = StringVar()

   new_dPS_statisticsTypesDiseases = StringVar()
   upd_dPS_statisticsTypesDiseases = StringVar()

#

   lbl_get_dPS = Label(dPS_app, text="Показать статистику работы отдела по id", font=font)
   entry_get_dPS = Entry(dPS_app, font=font, textvariable=get_id)
   btn_get_dPS = Button(dPS_app, text='Получить', font=font, command=lambda: fun_get_dPS(entry_get_dPS.get()))
   lbl_get_dPS.grid(row=1, column=1)
   entry_get_dPS.grid(row=2, column=0)
   btn_get_dPS.grid(row=2, column=1)

#

   lbl_new_dPS = Label(dPS_app, text='Добавить новую статистику работы отдела', font=font)

   lbl_new_dPS_NumberCompletedApplications = Label(dPS_app, text='Введите Количество заполненных заявок', font=font)
   entry_new_dPS_NumberCompletedApplications_data = Entry(dPS_app, font=font, textvariable=new_dPS_NumberCompletedApplications)

   lbl_new_dPS_AvgApplicationTime = Label(dPS_app, text='Введите Среднее время выполнение заявок', font=font)
   entry_new_dPS_AvgApplicationTime_data = Entry(dPS_app, font=font, textvariable=new_dPS_AvgApplicationTime)

   lbl_new_dPS_statisticsTypesDiseases = Label(dPS_app, text='Введите Статистику типов заболеваний', font=font)
   entry_new_dPS_statisticsTypesDiseases_data = Entry(dPS_app, font=font, textvariable=new_dPS_statisticsTypesDiseases)


#

   btn_new_dPS = Button(dPS_app, text='Создать', font=font, command=lambda: fun_new_dPS(entry_new_dPS_NumberCompletedApplications_data.get(),entry_new_dPS_AvgApplicationTime_data.get(),entry_new_dPS_statisticsTypesDiseases_data.get()))
   lbl_new_dPS.grid(row=3, column=1)

   lbl_new_dPS_NumberCompletedApplications.grid(row=4, column=0)
   entry_new_dPS_NumberCompletedApplications_data.grid(row=4, column=2)

   lbl_new_dPS_AvgApplicationTime.grid(row=5, column=0)
   entry_new_dPS_AvgApplicationTime_data.grid(row=5, column=2)

   lbl_new_dPS_statisticsTypesDiseases.grid(row=6, column=0)
   entry_new_dPS_statisticsTypesDiseases_data.grid(row=6, column=2)

   btn_new_dPS.grid(row=8, column=1)

#

   lbl_upd_dPS = Label(dPS_app, text='Обновить статистику работы отдела по id', font=font)

   lbl_upd_dPS_id = Label(dPS_app, text='Введите id статистики работы отдела', font=font)
   entry_upd_dPS = Entry(dPS_app, font=font, textvariable=upd_id)

   lbl_upd_dPS_NumberCompletedApplications = Label(dPS_app, text='Введите Количество заполненных заявок', font=font)
   entry_upd_dPS_NumberCompletedApplications_data = Entry(dPS_app, font=font, textvariable=upd_dPS_NumberCompletedApplications)

   lbl_upd_dPS_AvgApplicationTime = Label(dPS_app, text='Введите Среднее время выполнение заявок', font=font)
   entry_upd_dPS_AvgApplicationTime_data = Entry(dPS_app, font=font, textvariable=upd_dPS_AvgApplicationTime)

   lbl_upd_dPS_statisticsTypesDiseases = Label(dPS_app, text='Введите Статистику типов заболеваний', font=font)
   entry_upd_dPS_statisticsTypesDiseases_data = Entry(dPS_app, font=font, textvariable=upd_dPS_statisticsTypesDiseases)


#

   btn_upd_dPS = Button(dPS_app, text='Обновить', font=font, command=lambda: fun_upd_dPS(entry_upd_dPS.get(),entry_upd_dPS_NumberCompletedApplications_data.get(),entry_upd_dPS_AvgApplicationTime_data.get(),entry_upd_dPS_statisticsTypesDiseases_data.get()))
   lbl_upd_dPS.grid(row=9, column=1)

   lbl_upd_dPS_id.grid(row=10, column=0)
   entry_upd_dPS.grid(row=10, column=2)

   lbl_upd_dPS_NumberCompletedApplications.grid(row=11, column=0)
   entry_upd_dPS_NumberCompletedApplications_data.grid(row=11, column=2)

   lbl_upd_dPS_AvgApplicationTime.grid(row=12, column=0)
   entry_upd_dPS_AvgApplicationTime_data.grid(row=12, column=2)

   lbl_upd_dPS_statisticsTypesDiseases.grid(row=13, column=0)
   entry_upd_dPS_statisticsTypesDiseases_data.grid(row=13, column=2)

   btn_upd_dPS.grid(row=15, column=1)

#

   lbl_del_dPS = Label(dPS_app, text='Удалить статистику работы отдела по id', font=font)
   entry_del_dPS = Entry(dPS_app, font=font, textvariable=del_id)
   btn_del_dPS = Button(dPS_app, text='Удалить', font=font, command=lambda: fun_del_dPS(entry_del_dPS.get()))

   lbl_del_dPS.grid(row=16, column=1)
   entry_del_dPS.grid(row=17, column=0)
   btn_del_dPS.grid(row=17, column=1)


#
   global lb2_response
   lb1_response = Label(dPS_app, text='Полученный ответ', font=font)
   lb2_response = Label(dPS_app, text='', font=font)

   lb1_response.grid(row=18, column=1)
   lb2_response.grid(row=19, column=1)

def get_response(s):
   response = s
   print(response)
   lb2_response.config(text=response)

#

def fun_get_dPS(dPS_id):
   r = requests.get(f'http://127.0.0.1:8000/dPS/{dPS_id}')
   answer = r.json()
   get_response(answer)

def fun_new_dPS(NumberCompletedApplications,AvgApplicationTime,statisticsTypesDiseases):
   data = f'{{ "NumberCompletedApplications": "{NumberCompletedApplications}", "AvgApplicationTime": "{AvgApplicationTime}", "statisticsTypesDiseases": "{statisticsTypesDiseases}"}}'
   r = requests.post(f'http://127.0.0.1:8000/dPS/',data=data)
   answer = r.json()
   get_response(answer)

def fun_upd_dPS(dPS_id,NumberCompletedApplications,AvgApplicationTime,statisticsTypesDiseases):
   data = f'{{ "NumberCompletedApplications": "{NumberCompletedApplications}", "AvgApplicationTime": "{AvgApplicationTime}", "statisticsTypesDiseases": "{statisticsTypesDiseases}" }}'
   r = requests.put(f'http://127.0.0.1:8000/dPS/{dPS_id}',data=data)
   answer = r.json()
   get_response(answer)

def fun_del_dPS(dPS_id):
   r = requests.delete(f'http://127.0.0.1:8000/dPS/{dPS_id}')
   answer = r.json()
   get_response(answer)