pip install fastapi
pip install uvicorn
pip install requests

ИЛИ

(почему-то их здесь много)
pip install -r requirements.txt

Для запуска сервера:
Открыть src и запустить server.py

Для запуска GUI:
Открыть src/client и запустить mainwindow.py

Update 1.1.0
    + Проверки на даты,id 
    + сократил код для удобства - только для application
    + изменил дизайн - только для application
    + Русифицировал
    + requirements.txt
Update 1.2.0
    + Сделал динамический запрос sql - только для application

    - кнопка назад






Для себя:
    pip freeze > requirements.txt
    pip install -r requirements.txt