# Yeep

Простая и мощная библиотека для работы с PostgreSQL в Python.

## Возможности

- ✨ Простой и понятный API
- 📦 Автоматическое создание таблиц
- 🔄 Поддержка транзакций
- 🔍 Гибкий поиск и фильтрация
- 🔗 JOIN запросы
- 📊 Агрегатные функции
- 📈 Массовые операции
- 🛡️ Защита от SQL-инъекций

## Установка

```bash
pip install yeep
```

## Пример использования

```python
from yeep import PostgresDB, Table, Column, ColumnType

# Подключение к БД
db = PostgresDB(
    database="your_db",
    user="your_user",
    password="your_password",
    host="localhost",
    port=5432
)

# Схема таблицы
users_schema = [
    Column("id", ColumnType.SERIAL, primary_key=True),
    Column("name", ColumnType.VARCHAR, length=100),
    Column("email", ColumnType.VARCHAR, length=100, unique=True),
    Column("created_at", ColumnType.TIMESTAMP, default="CURRENT_TIMESTAMP")
]

# Работа с таблицей
with db:
    users = Table(db, "users", users_schema)
    
    # Создание записи
    user = users.insert({
        "name": "Иван",
        "email": "ivan@example.com"
    })
```

Подробная документация и примеры: [Wiki](https://github.com/TimaYeep/yeep/wiki)

## Лицензия

MIT 