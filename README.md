# 🚀 FreelanceHunter (GigCore)

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109-005571?style=for-the-badge&logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-7-DC382D?style=for-the-badge&logo=redis&logoColor=white)
![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)

**GigCore** — это высокопроизводительная платформа для фриланса с микросервисной архитектурой.
Проект включает в себя мощный **Backend API** (FastAPI) и современный **Frontend Client** (Vanilla JS + Tailwind), полностью упакованные в **Docker**.

---

## 📸 Демонстрация (UI)

> *Здесь будет скриншот твоего интерфейса. Сделай скрин сайта и положи его в папку `docs/screen.png`*
![Dashboard Interface](docs/screen.png)

---

## 🔥 Ключевые возможности

### 🛡️ Безопасность и Auth
- **JWT Authentication:** Полная защита API (Access Token + Refresh logic).
- **Secure Logout:** Реализован **Blacklist** токенов через **Redis**.
- **Password Hashing:** Использование **Bcrypt** для защиты данных пользователей.
- **Auto-Authoring:** Система автоматически привязывает создаваемые задачи к текущему пользователю (Anti-Spoofing).

### 🏗️ Архитектура и Инфраструктура
- **Clean Architecture:** Четкое разделение слоев (Router -> Service -> DB).
- **Dockerized:** Полная изоляция (App + DB + Redis) через `docker-compose`.
- **Async SQLAlchemy:** Полностью асинхронная работа с базой данных PostgreSQL.
- **Relationships:** Настроенные связи `One-to-Many` (User -> Jobs).

### 🎨 Frontend
- **Modern UI:** Темная тема (Dark Mode), Glassmorphism.
- **SPA Experience:** Работа без перезагрузки страницы (Fetch API).
- **Real-time Feedback:** Уведомления (Toasts) и динамическое обновление контента.

---

## 🛠 Технологический стек

| Category | Tech Stack |
|----------|------------|
| **Core** | Python 3.13, FastAPI (Async) |
| **Database** | PostgreSQL 16, SQLAlchemy 2.0 (Async Engine), Alembic |
| **Cache & Security** | Redis (Token Blacklist) |
| **Infrastructure** | Docker, Docker Compose |
| **Frontend** | HTML5, Vanilla JS, Tailwind CSS (CDN) |
| **Testing** | Pytest, Pytest-Asyncio |

---

## 🚀 Как запустить проект

### Вариант 1: Через Docker (Рекомендуемый) 🐳
Самый быстрый способ поднять всё окружение (БД, Редис, Бэкенд).

```bash
# 1. Клонировать репозиторий
git clone [https://github.com/almassuleimenov/freelance-hunter.git](https://github.com/almassuleimenov/freelance-hunter.git)

# 2. Запустить контейнеры
docker-compose up --build