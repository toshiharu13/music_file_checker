# API сервис проверки файлов music_file_checker
[![Python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)

##  Данная программа принимает музыкальный файл POST запросом и проверяет его на корректность. Ожидаемое расширение регулируется настройкой(по умолчанию WAV)

## Как установить
 - перейти в папку проекта
 - Склонировать проект
```shell
https://github.com/toshiharu13/music_file_checker.git
```
 - Установить requirements.txt
```shell
pip install -r requirements.txt
```
 - Создать файл .env и заполнить в нем переменные:
 
```dotenv
SECRET_KEY = 'ключ безопасности Django(по умолчанию replaceme)'
```
```dotenv
DEBUG = 'маркер дебага(по умолчанию True)'
```
```dotenv
ALLOWED_HOSTS = 'список разрешенных хостов(По умолчанию локальный хост)'
```

## Для запуска из папки проекта запутите команду:
```django
python manage.py runserver
```

## Документация по API запросам:
 - Сервер слушает POST запросы на http://server/api/v1/upload/ и принимает поле file с телом запроса(загружаемым файлом)
 - К примеру, локально развернутый сервер слушает на http://127.0.0.1:8000/api/v1/upload/
 - Динамическая документация по адресу http://server/redoc/
 - Примеры тестовых файлов и команд в папке testfolder

## Проект создан в качестве тестового задания



