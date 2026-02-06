# FreelanceHunter (GigCore) 🚀 MVP

![Python](https://img.shields.io/badge/Python-3.13-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue)
![Security](https://img.shields.io/badge/Security-JWT_Auth-red)
![Tests](https://img.shields.io/badge/Tests-Pytest-yellow)

**GigCore** — это современный Backend API для фриланс-биржи, построенный на **Clean Architecture**.
Проект разработан с упором на асинхронность, безопасность и масштабируемость.

## 🔥 Ключевые возможности (New!)
- 🔐 **JWT Authentication:** Полная защита API с использованием Access Token.
- 🛡️ **Secure Password Hashing:** Связка SHA256 + Bcrypt для защиты данных.
- 👮‍♂️ **Dependency Injection:** Автоматическая валидация юзера при запросах.
- 🏛 **Clean Architecture:** Четкое разделение слоев (Router -> Service -> DB).

## 🛠 Технологический стек

- **Language:** Python 3.13
- **Framework:** FastAPI (Asynchronous)
- **Database:** PostgreSQL + SQLAlchemy 2.0 (Async Engine)
- **Migrations:** Alembic
- **Validation:** Pydantic v2
- **Testing:** Pytest + Pytest-Asyncio + HTTPX
- **Dependency Management:** Poetry

## 🏛 Архитектура

Проект следует принципам **Clean Architecture** и разделен на слои:
- `api/` — Роутеры и обработка HTTP-запросов (Presentation Layer).
- `services/` — Бизнес-логика приложения (Business Logic Layer).
- `schemas/` — DTO (Data Transfer Objects) для валидации данных.
- `models/` — ORM модели базы данных.
- `db/` — Настройки подключения и сессий БД.
