## Сервис, который позволит бизнесу создать тендер на оказание каких-либо услуг.

## Стек использованных технологий

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Django REST Framework](https://img.shields.io/badge/Django%20REST%20Framework-ff1709?style=for-the-badge&logo=django&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-269539?style=for-the-badge&logo=nginx&logoColor=white)

## Описание проекта
Данный проект реализует HTTP API для сервиса проведения тендеров. Он позволяет организациям создавать тендеры на оказание услуг, а пользователям и другим компаниям предлагать свои условия для участия в тендерах.

## Основной функционал:
- Пользователи и организации: Поддержка создания пользователей и организаций.
- Тендеры: Возможность создания, редактирования, публикации и закрытия тендеров от имени организации.
- Предложения: Пользователи могут делать предложения по тендерам от имени своей организации, а также редактировать и публиковать их.
- Откат версий: Поддержка отката тендеров и предложений до предыдущих версий.
- Отзывы: Возможность просмотра и оставления - отзывов на предложения.

C более подробным функционалом работающего приложения можно ознакомиться в папке "задание" файл "README.md"

### Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
```bash
git clone https://github.com/MoskvinaAnastasia/Avito-Tender-service
```
Cоздать и активировать виртуальное окружение:
```bash
python -m venv env
source venv/Scripts/activate
```
Установить зависимости из файла requirements.txt:
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```
Выполнить миграции:
```bash
python manage.py migrate
```