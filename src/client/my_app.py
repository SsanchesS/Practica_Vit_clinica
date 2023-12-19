from tkinter import *
from  api.application_api import create_application_app
from  api.applicationPrivate_api import create_applicationPrivate_app
from  api.veterinarian_api import create_veterinarian_app
from  api.departmentPerformanceStatistics_api import create_dPS_app
from  api.user_api import create_user_app


def create_app(root,font,user_props):
  app = Toplevel(root)
  app.title("Выберите запрос")  
  app.geometry('700x400')

  def f_application_app():
    app.withdraw()
    create_application_app(root,font)

  def f_applicationPrivate_app():
    app.withdraw()
    create_applicationPrivate_app(root,font)
  
  def f_veterinarian_app():
    app.withdraw()
    create_veterinarian_app(root,font)

  def f_dPS_app():
    app.withdraw()
    create_dPS_app(root,font)

  def f_user_app():
    app.withdraw()
    create_user_app(root,font,user_props)

  btn_app_albums = Button(app, text='Заявка', font=font, command=f_application_app)

  btn_app_albums.grid(row=1, column=0)

  if(user_props["role_id"]==1):
    btn_app_albums = Button(app, text='Заявка расширенная', font=font, command=f_applicationPrivate_app)

    btn_app_albums.grid(row=1, column=1)

    btn_app_artists = Button(app, text='Ветеринар', font=font, command=f_veterinarian_app)

    btn_app_artists.grid(row=2, column=0)

    btn_app_songs = Button(app, text='Статистика работы отдела', font=font, command=f_dPS_app)

    btn_app_songs.grid(row=2, column=1)

  btn_app_customer = Button(app, text='Пользователи', font=font, command=f_user_app)

  btn_app_customer.grid(row=3, column=0)
