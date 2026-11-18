# Order Processing Service

Современный backend-сервис для обработки заказов, разработанный как модернизация legacy-скрипта `legacy_process_order.php`.

## Описание проекта

Исходный скрипт представлял собой монолитный PHP-файл без архитектуры, валидации, тестов и защиты от SQL-инъекций.  
В рамках проекта он был переработан в современный API-сервис на **FastAPI** с разделением ответственности, безопасной обработкой данных, тестами и документацией.

## Цели модернизации

- устранить SQL-инъекции;
- добавить валидацию входных данных;
- реализовать современную архитектуру;
- вынести бизнес-логику в отдельный сервис;
- покрыть критическую функциональность тестами;
- подготовить документацию API;
- сделать код поддерживаемым и расширяемым.

## Стек технологий

- **Python 3.12**
- **FastAPI**
- **Pydantic**
- **SQLAlchemy**
- **PostgreSQL** / SQLite (для локальной разработки и тестов)
- **Pytest**
- **Uvicorn**

## Архитектура проекта

Используется подход:

- `routers` — HTTP-слой;
- `services` — бизнес-логика;
- `repositories` — работа с базой данных;
- `schemas` — входные и выходные DTO;
- `models` — ORM-модели;
- `tests` — unit и API тесты.

Принцип: **тонкий роутер → толстый сервис → репозиторий**

## Структура проекта

```bash
app/
├── main.py
├── routers/
│   └── orders.py
├── services/
│   └── order_service.py
├── repositories/
│   ├── order_repository.py
│   └── product_repository.py
├── schemas/
│   └── order.py
├── models/
│   ├── order.py
│   ├── order_item.py
│   └── product.py
└── db/
    └── session.py

tests/
├── test_order_service.py
└── test_orders_api.py

README.md
STRATEGY.md
requirements.txt