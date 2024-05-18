# Укорачиватель ссылок

Сайт на котором любой желающий может укоротить ссылку своей любимой страницы до 6 символов!

## Технологии

* Python
* Flask
* WTForms
* SQLAlchemy

## Как запустить

1. Склонируйте репозиторий
2. Создайте и активируйте виртуальное окружение
```commandline
python -m venv venv
source venv/Scripts/activate
```  
3. Установите зависимости
```commandline
pip install -r requirements.txt
```
4. Создайте файл .env и укажите настройки подключения к БД и другие параметры.
```commandline
DATABASE_URI = sqlite:///urls.db
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = tu849gj9i4
```
5. Запустите flask приложение
```commandline
flask run
```

## Автор

Я™
