# ProjectXB

## Описание

Краткое описание вашего проекта. Укажите, для чего он предназначен и какие основные функции реализованы.

## Требования

Перед началом работы убедитесь, что на вашем компьютере установлены следующие программы:

- Python 3.12+
- Git
- PostgreSQL (если используете PostgreSQL в качестве базы данных)

## Установка

###  Клонирование репозитория

Сначала клонируйте репозиторий на свой локальный компьютер:

```bash
git clone https://github.com/your-username/projectXB.git
cd projectXB
```
### Создание виртуального окружения

### Установка зависимостей
```bash
pip install -r requirements.txt

```

### Применение миграций
```bash
python manage.py migrate

```
### Создание суперпользователя
```bash
python manage.py createsuperuser

```
### Запуск сервера
```bash
python manage.py runserver
```
### Документация API

Swagger UI: http://127.0.0.1:8000/swagger/
Redoc: http://127.0.0.1:8000/redoc/





