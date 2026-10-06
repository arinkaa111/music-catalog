MUSIC CATALOG

Небольшой веб-каталог для музыки: артисты, альбомы и треки. Делала как учебный проект по «Проектному практикуму» — постепенно, от простого FastAPI-приложения до рабочего продукта с базой данных и фронтом.


О ПРОЕКТЕ

Идея простая: надоело, что любимая музыка разбросана по разным сервисам и плейлистам. Хотелось иметь одно место, где можно собрать свой каталог — с артистами, альбомами и треками, с быстрым поиском.

Получилось веб-приложение, где можно смотреть список артистов и треков, добавлять новых артистов прямо со страницы, удалять треки. Всё работает через REST API и хранится в PostgreSQL.


ВОЗМОЖНОСТИ

Список артистов с фильтрацией по ID
Список треков с фильтром по жанру
Добавление артиста через форму на странице
Добавление трека (нужен существующий album_id)
Удаление трека
Автодокументация Swagger на /docs
Тесты на основные сценарии


СТЕК ТЕХНОЛОГИЙ

Backend:
Python 3.13
FastAPI
SQLAlchemy 2.0
Pydantic для валидации
Alembic для миграций

База данных:
PostgreSQL 16 через Docker

Frontend:
Чистый HTML, CSS и JavaScript. Без сборки — просто открыл и работает.

Тесты:
Pytest и httpx

Инфраструктура:
Docker Compose для базы данных
Git и GitHub


СТРУКТУРА ПРОЕКТА

music-catalog/
  backend/
    app/
      config.py         — настройки, чтение .env
      database.py       — подключение к PostgreSQL
      schemas.py        — Pydantic-схемы
      models/
        __init__.py     — Artist, Album, Track
      routers/
        artists.py
        tracks.py
    alembic/            — миграции
    tests/
      conftest.py
      test_artists.py
      test_tracks.py
    main.py
    requirements.txt
    .env.example
    alembic.ini
  frontend/
    index.html          — весь фронт в одном файле
  docker-compose.yml
  user_story.md
  README.md


ПЕРЕМЕННЫЕ ОКРУЖЕНИЯ

Все настройки в backend/.env:

DATABASE_URL=postgresql+psycopg://music_user:music_pass@localhost:5433/music_catalog
TEST_DATABASE_URL=postgresql+psycopg://music_user:music_pass@localhost:5433/music_catalog_test

Порт 5433, а не стандартный 5432 — потому что на 5432 у меня сидит локальный PostgreSQL, и контейнер с ним конфликтует. Если у тебя такой проблемы нет, можешь использовать 5432.


КАК ЗАПУСТИТЬ ПРОЕКТ

Шаг 1. Клонировать репозиторий

git clone https://github.com/arinkaa111/music-catalog.git
cd music-catalog

Шаг 2. Поднять базу данных

docker compose up -d

Проверить, что контейнер поднялся:

docker ps

Шаг 3. Настроить .env

cd backend
cp .env.example .env

Открой .env и заполни своими значениями (по умолчанию — как в docker-compose.yml).

Шаг 4. Установить зависимости

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Шаг 5. Создать тестовую БД

docker exec -it music_catalog_db psql -U music_user -d music_catalog -c "CREATE DATABASE music_catalog_test;"

Шаг 6. Применить миграции

alembic upgrade head

Шаг 7. Запустить сервер

uvicorn main:app --reload

Сервер: http://127.0.0.1:8000
Swagger: http://127.0.0.1:8000/docs

Шаг 8. Открыть фронт

Просто открой frontend/index.html в браузере. Никакой сборки не нужно.

Или из терминала:

open frontend/index.html

Шаг 9. Запустить тесты

cd backend
source venv/bin/activate
pytest -v

Должно быть 7 passed.


ЧТО МОЖНО УЛУЧШИТЬ

Проект учебный, но если развивать:

Добавить CRUD для альбомов (сейчас только модели, без роутера)
Авторизацию и личные плейлисты
Загрузку аудиофайлов
Пагинацию в списках
Поиск по подстроке, а не только фильтр по ID


АВТОР

Арина — backend, frontend и тесты. Проект сделан в рамках дисциплины «Проектный практикум», 6 семестр.