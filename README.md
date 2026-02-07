# FreelanceHunter (GigCore) 🚀 MVP

![Python](https://img.shields.io/badge/Python-3.13-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue)
![Redis](https://img.shields.io/badge/Redis-7-red)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED)
![Security](https://img.shields.io/badge/Security-JWT_Auth-red)

**GigCore** — это современный Backend API для фриланс-биржи, построенный на **Clean Architecture**.
Проект разработан с упором на асинхронность, безопасность и микросервисную архитектуру.

## 🔥 Ключевые возможности (Update!)
- 🔐 **JWT Authentication:** Полная защита API (Access Token).
- 🚫 **Logout System:** Реализован **безопасный выход** через Blacklist токенов (Redis).
- 🐳 **Dockerized:** Полная изоляция инфраструктуры (App + DB + Redis) через Docker Compose.
- 🛡️ **Secure Password Hashing:** Надежное хеширование паролей (Bcrypt).
- 🏛 **Clean Architecture:** Четкое разделение слоев (Router -> Service -> DB).

## 🛠 Технологический стек

- **Language:** Python 3.13
- **Framework:** FastAPI (Asynchronous)
- **Database:** PostgreSQL + SQLAlchemy 2.0 (Async Engine)
- **Cache & Security:** Redis (для Blacklist токенов)
- **Infrastructure:** Docker & Docker Compose
- **Migrations:** Alembic
- **Validation:** Pydantic v2
- **Testing:** Pytest + Pytest-Asyncio

## 🏛 Архитектура

Проект следует принципам **Clean Architecture**:
- `api/` — Роутеры и обработка HTTP-запросов (Presentation Layer).
- `services/` — Бизнес-логика приложения (Business Logic Layer).
- `schemas/` — DTO (Data Transfer Objects) для валидации данных.
- `models/` — ORM модели базы данных.
- `core/` — Глобальные настройки (Config, Security).