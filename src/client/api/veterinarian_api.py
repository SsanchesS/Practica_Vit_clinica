import requests
from tkinter import *

def create_veterinarian_app(root,font):
   veterinarian_app = Toplevel(root)
   veterinarian_app.title("Работа с veterinarian")  
   veterinarian_app.geometry('1400x700')


   get_id = StringVar()
   upd_id = StringVar()
   del_id = StringVar()

   new_veterinarian_name = StringVar()
   upd_veterinarian_name = StringVar()


#

   lbl_get_veterinarian = Label(veterinarian_app, text="Показать veterinarian по id", font=font)
   entry_get_veterinarian = Entry(veterinarian_app, font=font, textvariable=get_id)
   btn_get_veterinarian = Button(veterinarian_app, text='Получить', font=font, command=lambda: fun_get_veterinarian(entry_get_veterinarian.get()))
   lbl_get_veterinarian.grid(row=1, column=1)
   entry_get_veterinarian.grid(row=2, column=0)
   btn_get_veterinarian.grid(row=2, column=1)

#

   lbl_new_veterinarian = Label(veterinarian_app, text='Добавить нового veterinarian', font=font)

   lbl_new_veterinarian_name = Label(veterinarian_app, text='Введите name нового veterinarian', font=font)
   entry_new_veterinarian_name_data = Entry(veterinarian_app, font=font, textvariable=new_veterinarian_name)

#

   btn_new_veterinarian = Button(veterinarian_app, text='Создать', font=font, command=lambda: fun_new_veterinarian(entry_new_veterinarian_name_data.get()))
   lbl_new_veterinarian.grid(row=3, column=1)

   lbl_new_veterinarian_name.grid(row=4, column=0)
   entry_new_veterinarian_name_data.grid(row=4, column=2)


   btn_new_veterinarian.grid(row=6, column=1)

#

   lbl_upd_veterinarian = Label(veterinarian_app, text='Обновить veterinarian по id', font=font)

   lbl_upd_veterinarian_id = Label(veterinarian_app, text='Введите veterinarian_id', font=font)
   entry_upd_veterinarian = Entry(veterinarian_app, font=font, textvariable=upd_id)

   lbl_upd_veterinarian_name = Label(veterinarian_app, text='Введите name veterinarian', font=font)
   entry_upd_veterinarian_name_data = Entry(veterinarian_app, font=font, textvariable=upd_veterinarian_name)



#

   btn_upd_veterinarian = Button(veterinarian_app, text='Обновить', font=font, command=lambda: fun_upd_veterinarian(entry_upd_veterinarian.get(),entry_upd_veterinarian_name_data.get()))
   lbl_upd_veterinarian.grid(row=8, column=1)

   lbl_upd_veterinarian_id.grid(row=9, column=0)
   entry_upd_veterinarian.grid(row=9, column=2)

   lbl_upd_veterinarian_name.grid(row=10, column=0)
   entry_upd_veterinarian_name_data.grid(row=10, column=2)


   btn_upd_veterinarian.grid(row=12, column=1)

#

   lbl_del_veterinarian = Label(veterinarian_app, text='Удалить veterinarian по id', font=font)
   entry_del_veterinarian = Entry(veterinarian_app, font=font, textvariable=del_id)
   btn_del_veterinarian = Button(veterinarian_app, text='Удалить', font=font, command=lambda: fun_del_veterinarian(entry_del_veterinarian.get()))

   lbl_del_veterinarian.grid(row=14, column=1)
   entry_del_veterinarian.grid(row=15, column=0)
   btn_del_veterinarian.grid(row=15, column=1)


#
   global lb2_response
   lb1_response = Label(veterinarian_app, text='Полученный ответ', font=font)
   lb2_response = Label(veterinarian_app, text='', font=font)

   lb1_response.grid(row=16, column=1)
   lb2_response.grid(row=17, column=1)

def get_response(s):
   response = s
   print(response)
   lb2_response.config(text=response)

#

def fun_get_veterinarian(veterinarian_id):
   r = requests.get(f'http://127.0.0.1:8000/veterinarian/{veterinarian_id}')
   answer = r.json()
   get_response(answer)

def fun_new_veterinarian(name):
   data = f'{{ "name": "{name}"}}'
   r = requests.post(f'http://127.0.0.1:8000/veterinarian/',data=data)
   answer = r.json()
   get_response(answer)

def fun_upd_veterinarian(veterinarian_id,name):
   data = f'{{ "name": "{name}"}}'
   r = requests.put(f'http://127.0.0.1:8000/veterinarian/{veterinarian_id}',data=data)
   answer = r.json()
   get_response(answer)

def fun_del_veterinarian(veterinarian_id):
   r = requests.delete(f'http://127.0.0.1:8000/veterinarian/{veterinarian_id}')
   answer = r.json()
   get_response(answer)