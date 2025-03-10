from typing import Optional, List, Dict, Any, Union, Tuple
from .database import PostgresDB
from enum import Enum
from datetime import datetime

class Operator(Enum):
    EQ = "="
    NEQ = "!="
    GT = ">"
    GTE = ">="
    LT = "<"
    LTE = "<="
    LIKE = "LIKE"
    ILIKE = "ILIKE"
    IN = "IN"
    NOT_IN = "NOT IN"
    BETWEEN = "BETWEEN"
    IS_NULL = "IS NULL"
    IS_NOT_NULL = "IS NOT NULL"

class Condition:
    def __init__(self, column: str, operator: Operator, value: Any = None):
        self.column = column
        self.operator = operator
        self.value = value

class JoinType(Enum):
    INNER = "INNER JOIN"
    LEFT = "LEFT JOIN"
    RIGHT = "RIGHT JOIN"
    FULL = "FULL JOIN"

class ColumnType(Enum):
    INTEGER = "INTEGER"
    BIGINT = "BIGINT"
    SERIAL = "SERIAL"
    BIGSERIAL = "BIGSERIAL"
    TEXT = "TEXT"
    VARCHAR = "VARCHAR"
    BOOLEAN = "BOOLEAN"
    TIMESTAMP = "TIMESTAMP"
    DATE = "DATE"
    NUMERIC = "NUMERIC"
    JSONB = "JSONB"
    UUID = "UUID"

class Column:
    SPECIAL_DEFAULTS = {
        "CURRENT_TIMESTAMP",
        "CURRENT_DATE",
        "CURRENT_TIME",
        "NULL",
        "TRUE",
        "FALSE"
    }

    def __init__(
        self,
        name: str,
        type: ColumnType,
        primary_key: bool = False,
        nullable: bool = True,
        unique: bool = False,
        default: Any = None,
        length: int = None,
        references: Tuple[str, str] = None
    ):
        self.name = name
        self.type = type
        self.primary_key = primary_key
        self.nullable = nullable
        self.unique = unique
        self.default = default
        self.length = length
        self.references = references

    def to_sql(self) -> str:
        """Преобразование определения колонки в SQL"""
        parts = [self.name]
        
        if self.type == ColumnType.VARCHAR and self.length:
            parts.append(f"{self.type.value}({self.length})")
        else:
            parts.append(self.type.value)
            
        if self.primary_key:
            parts.append("PRIMARY KEY")
            
        if not self.nullable:
            parts.append("NOT NULL")
            
        if self.unique:
            parts.append("UNIQUE")
            
        if self.default is not None:
            if isinstance(self.default, str):
                if self.default.upper() in self.SPECIAL_DEFAULTS:
                    parts.append(f"DEFAULT {self.default}")
                else:
                    parts.append(f"DEFAULT '{self.default}'")
            else:
                parts.append(f"DEFAULT {self.default}")
                
        if self.references:
            table, column = self.references
            parts.append(f"REFERENCES {table}({column})")
            
        return " ".join(parts)

class Table:
    def __init__(self, db: PostgresDB, table_name: str, schema: List[Column] = None):
        """
        Инициализация работы с таблицей
        
        :param db: Экземпляр подключения к базе данных
        :param table_name: Имя таблицы
        :param schema: Схема таблицы (список колонок)
        """
        self.db = db
        self.table_name = table_name
        self.schema = schema
        if schema:
            self._ensure_table()

    def _ensure_table(self) -> None:
        """Создание таблицы, если она не существует"""
        if not self.schema:
            return
            
        columns_sql = ",\n    ".join(col.to_sql() for col in self.schema)
        query = f"""
            CREATE TABLE IF NOT EXISTS {self.table_name} (
                {columns_sql}
            )
        """
        self.db.execute(query)

    def alter_table(self, new_columns: List[Column]) -> None:
        """
        Изменение структуры таблицы
        
        :param new_columns: Список новых колонок
        """
        existing_columns = {col['column_name']: col for col in self.get_columns()}
        
        for column in new_columns:
            if column.name not in existing_columns:
                query = f"ALTER TABLE {self.table_name} ADD COLUMN {column.to_sql()}"
                self.db.execute(query)

    def _build_where_clause(self, conditions: Union[Dict[str, Any], List[Condition]]) -> Tuple[str, list]:
        """Построение WHERE условия"""
        if not conditions:
            return "", []

        params = []
        if isinstance(conditions, dict):
            where_clauses = []
            for column, value in conditions.items():
                if isinstance(value, (list, tuple)):
                    placeholders = ", ".join(["%s"] * len(value))
                    where_clauses.append(f"{column} IN ({placeholders})")
                    params.extend(value)
                elif value is None:
                    where_clauses.append(f"{column} IS NULL")
                else:
                    where_clauses.append(f"{column} = %s")
                    params.append(value)
            where_sql = " AND ".join(where_clauses)
        else:
            where_clauses = []
            for condition in conditions:
                if condition.operator in [Operator.IS_NULL, Operator.IS_NOT_NULL]:
                    where_clauses.append(f"{condition.column} {condition.operator.value}")
                elif condition.operator == Operator.BETWEEN:
                    where_clauses.append(f"{condition.column} BETWEEN %s AND %s")
                    params.extend(condition.value)
                elif condition.operator in [Operator.IN, Operator.NOT_IN]:
                    placeholders = ", ".join(["%s"] * len(condition.value))
                    where_clauses.append(f"{condition.column} {condition.operator.value} ({placeholders})")
                    params.extend(condition.value)
                else:
                    where_clauses.append(f"{condition.column} {condition.operator.value} %s")
                    params.append(condition.value)
            where_sql = " AND ".join(where_clauses)

        return where_sql, params

    def find_with_join(self,
                      joins: List[Tuple[str, str, JoinType, str]],
                      conditions: Union[Dict[str, Any], List[Condition]] = None,
                      columns: List[str] = None,
                      order_by: Union[str, List[str]] = None,
                      limit: int = None,
                      offset: int = None) -> List[Dict[str, Any]]:
        """
        Поиск с JOIN
        
        :param joins: Список кортежей (таблица, условие соединения, тип соединения, алиас)
        :param conditions: Условия фильтрации
        :param columns: Список колонок
        :param order_by: Сортировка
        :param limit: Лимит
        :param offset: Смещение
        :return: Результаты запроса
        """
        select_columns = "*" if not columns else ", ".join(columns)
        query = f"SELECT {select_columns} FROM {self.table_name}"
        
        for table, on_clause, join_type, alias in joins:
            # Заменяем имя таблицы на алиас в условии соединения, если он есть
            if alias and table in on_clause:
                on_clause = on_clause.replace(table + ".", alias + ".")
            query += f" {join_type.value} {table}"
            if alias:
                query += f" AS {alias}"
            query += f" ON {on_clause}"

        params = []
        if conditions:
            where_sql, where_params = self._build_where_clause(conditions)
            if where_sql:
                query += f" WHERE {where_sql}"
                params.extend(where_params)

        if order_by:
            if isinstance(order_by, list):
                query += f" ORDER BY {', '.join(order_by)}"
            else:
                query += f" ORDER BY {order_by}"

        if limit is not None:
            query += f" LIMIT {limit}"

        if offset is not None:
            query += f" OFFSET {offset}"

        results = self.db.fetch_all(query, tuple(params) if params else None)
        return [format_dict(result) for result in results]

    def aggregate(self,
                 aggregations: List[Tuple[str, str, str]],
                 group_by: List[str] = None,
                 having: List[Condition] = None,
                 conditions: Union[Dict[str, Any], List[Condition]] = None) -> List[Dict[str, Any]]:
        """
        Выполнение агрегатных запросов
        
        :param aggregations: Список кортежей (функция, колонка, алиас)
        :param group_by: Список колонок для группировки
        :param having: Условия для HAVING
        :param conditions: Условия фильтрации
        :return: Результаты агрегации
        """
        agg_columns = [f"{func}({col}) AS {alias}" for func, col, alias in aggregations]
        if group_by:
            agg_columns.extend(group_by)
        
        query = f"SELECT {', '.join(agg_columns)} FROM {self.table_name}"
        params = []

        if conditions:
            where_sql, where_params = self._build_where_clause(conditions)
            if where_sql:
                query += f" WHERE {where_sql}"
                params.extend(where_params)

        if group_by:
            query += f" GROUP BY {', '.join(group_by)}"

        if having:
            having_sql, having_params = self._build_where_clause(having)
            if having_sql:
                query += f" HAVING {having_sql}"
                params.extend(having_params)

        return self.db.fetch_all(query, tuple(params) if params else None)

    def find_many(self,
                 conditions: Union[Dict[str, Any], List[Condition]] = None,
                 order_by: Union[str, List[str]] = None,
                 limit: int = None,
                 offset: int = None,
                 columns: List[str] = None) -> List[Dict[str, Any]]:
        """
        Найти записи по условиям
        
        :param conditions: Словарь с условиями или список объектов Condition
        :param order_by: Строка или список строк для сортировки
        :param limit: Ограничение количества записей
        :param offset: Смещение от начала
        :param columns: Список колонок для выборки
        :return: Список найденных записей
        """
        select_columns = "*" if not columns else ", ".join(columns)
        query = f"SELECT {select_columns} FROM {self.table_name}"
        
        params = []
        if conditions:
            where_sql, where_params = self._build_where_clause(conditions)
            if where_sql:
                query += f" WHERE {where_sql}"
                params.extend(where_params)

        if order_by:
            if isinstance(order_by, list):
                query += f" ORDER BY {', '.join(order_by)}"
            else:
                query += f" ORDER BY {order_by}"

        if limit is not None:
            query += f" LIMIT {limit}"

        if offset is not None:
            query += f" OFFSET {offset}"

        results = self.db.fetch_all(query, tuple(params) if params else None)
        return [format_dict(result) for result in results]

    def transaction(self):
        """Контекстный менеджер для транзакций"""
        return Transaction(self.db)

    def insert(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Вставка новой записи в таблицу
        
        :param data: Словарь с данными для вставки {колонка: значение}
        :return: Созданная запись
        """
        columns = list(data.keys())
        values = list(data.values())
        placeholders = ["%s"] * len(columns)
        
        query = f"""
            INSERT INTO {self.table_name} ({', '.join(columns)})
            VALUES ({', '.join(placeholders)})
            RETURNING *
        """
        result = self.db.fetch_one(query, tuple(values))
        return format_dict(result) if result else None

    def insert_many(self, data_list: List[Dict[str, Any]], batch_size: int = 1000) -> List[Dict[str, Any]]:
        """
        Массовая вставка записей с поддержкой батчей
        
        :param data_list: Список словарей с данными
        :param batch_size: Размер пакета для вставки
        :return: Список созданных записей
        """
        if not data_list:
            return []
            
        results = []
        for i in range(0, len(data_list), batch_size):
            batch = data_list[i:i + batch_size]
            columns = list(batch[0].keys())
            values_list = [tuple(item[col] for col in columns) for item in batch]
            placeholders = ["%s"] * len(columns)
            
            query = f"""
                INSERT INTO {self.table_name} ({', '.join(columns)})
                VALUES ({', '.join(placeholders)})
                RETURNING *
            """
            
            for values in values_list:
                result = self.db.fetch_one(query, values)
                if result:
                    results.append(format_dict(result))
        return results

    def find_one(self, conditions: Dict[str, Any] = None) -> Optional[Dict[str, Any]]:
        """
        Найти одну запись по условиям
        
        :param conditions: Словарь с условиями {колонка: значение}
        :return: Найденная запись или None
        """
        query = f"SELECT * FROM {self.table_name}"
        params = []
        
        if conditions:
            where_clauses = []
            for column, value in conditions.items():
                if value is None:
                    where_clauses.append(f"{column} IS NULL")
                else:
                    where_clauses.append(f"{column} = %s")
                    params.append(value)
            query += " WHERE " + " AND ".join(where_clauses)
            
        result = self.db.fetch_one(query, tuple(params) if params else None)
        return format_dict(result) if result else None

    def update(self, conditions: Dict[str, Any], data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Обновить записи по условиям
        
        :param conditions: Словарь с условиями {колонка: значение}
        :param data: Словарь с новыми данными {колонка: значение}
        :return: Список обновленных записей
        """
        set_clauses = []
        params = []
        
        for column, value in data.items():
            if value is None:
                set_clauses.append(f"{column} = NULL")
            else:
                set_clauses.append(f"{column} = %s")
                params.append(value)
            
        where_clauses = []
        for column, value in conditions.items():
            if value is None:
                where_clauses.append(f"{column} IS NULL")
            else:
                where_clauses.append(f"{column} = %s")
                params.append(value)
            
        query = f"""
            UPDATE {self.table_name}
            SET {', '.join(set_clauses)}
            WHERE {' AND '.join(where_clauses)}
            RETURNING *
        """
        
        results = self.db.fetch_all(query, tuple(params))
        return [format_dict(result) for result in results]

    def update_many(self, updates: List[Dict[str, Any]], key_column: str) -> List[Dict[str, Any]]:
        """
        Массовое обновление записей
        
        :param updates: Список словарей с данными для обновления
        :param key_column: Колонка, по которой идентифицируются записи
        :return: Список обновленных записей
        """
        if not updates:
            return []

        # Собираем все колонки для обновления
        all_columns = set()
        for update in updates:
            all_columns.update(update.keys())
        all_columns.remove(key_column)
        
        # Формируем CASE выражения для каждой колонки
        case_statements = []
        params = []
        key_values = []
        
        for column in all_columns:
            when_clauses = []
            for update in updates:
                if column in update:
                    when_clauses.append(f"WHEN {key_column} = %s THEN %s")
                    params.extend([update[key_column], update[column]])
                    if update[key_column] not in key_values:
                        key_values.append(update[key_column])
            
            if when_clauses:
                case_statements.append(
                    f"{column} = (CASE {' '.join(when_clauses)} ELSE {column} END)"
                )
        
        placeholders = ", ".join(["%s"] * len(key_values))
        query = f"""
            UPDATE {self.table_name}
            SET {', '.join(case_statements)}
            WHERE {key_column} IN ({placeholders})
            RETURNING *
        """
        params.extend(key_values)
        
        results = self.db.fetch_all(query, tuple(params))
        return [format_dict(result) for result in results]

    def delete(self, conditions: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Удалить записи по условиям
        
        :param conditions: Словарь с условиями {колонка: значение}
        :return: Список удаленных записей
        """
        where_clauses = []
        params = []
        
        for column, value in conditions.items():
            if isinstance(value, (list, tuple)):
                placeholders = ", ".join(["%s"] * len(value))
                where_clauses.append(f"{column} IN ({placeholders})")
                params.extend(value)
            elif value is None:
                where_clauses.append(f"{column} IS NULL")
            else:
                where_clauses.append(f"{column} = %s")
                params.append(value)
            
        query = f"""
            DELETE FROM {self.table_name}
            WHERE {' AND '.join(where_clauses)}
            RETURNING *
        """
        
        results = self.db.fetch_all(query, tuple(params))
        return [format_dict(result) for result in results]

    def count(self, conditions: Dict[str, Any] = None) -> int:
        """
        Подсчитать количество записей по условиям
        
        :param conditions: Словарь с условиями {колонка: значение}
        :return: Количество записей
        """
        query = f"SELECT COUNT(*) as count FROM {self.table_name}"
        params = []
        
        if conditions:
            where_clauses = []
            for column, value in conditions.items():
                if isinstance(value, (list, tuple)):
                    placeholders = ", ".join(["%s"] * len(value))
                    where_clauses.append(f"{column} IN ({placeholders})")
                    params.extend(value)
                elif value is None:
                    where_clauses.append(f"{column} IS NULL")
                else:
                    where_clauses.append(f"{column} = %s")
                    params.append(value)
            query += " WHERE " + " AND ".join(where_clauses)
            
        result = self.db.fetch_one(query, tuple(params) if params else None)
        return result['count'] if result else 0

    def exists(self, conditions: Dict[str, Any]) -> bool:
        """
        Проверить существование записи по условиям
        
        :param conditions: Словарь с условиями {колонка: значение}
        :return: True если запись существует, False если нет
        """
        return self.count(conditions) > 0

    def truncate(self) -> None:
        """
        Очистить таблицу
        """
        self.db.execute(f"TRUNCATE TABLE {self.table_name}")

    def get_columns(self) -> List[Dict[str, Any]]:
        """
        Получить информацию о колонках таблицы
        
        :return: Список словарей с информацией о колонках
        """
        query = """
            SELECT column_name, data_type, is_nullable
            FROM information_schema.columns
            WHERE table_name = %s
            ORDER BY ordinal_position
        """
        return self.db.fetch_all(query, (self.table_name,))

class Transaction:
    def __init__(self, db: PostgresDB):
        self.db = db

    def __enter__(self):
        self.db.execute("BEGIN")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.db.execute("COMMIT")
        else:
            self.db.execute("ROLLBACK")
            return False

def format_value(value: Any) -> str:
    """Форматирование значения для вывода"""
    if isinstance(value, datetime):
        return value.strftime("%Y-%m-%d %H:%M:%S")
    if value is None:
        return "NULL"
    return str(value)

def format_dict(data: Dict[str, Any]) -> Dict[str, Any]:
    """Форматирование словаря для вывода"""
    return {k: format_value(v) for k, v in data.items()} 