import psycopg2
from psycopg2.extras import RealDictCursor
from typing import Optional, Dict, List, Any
import os
from dotenv import load_dotenv

class PostgresDB:
    def __init__(self, database: str, user: str, password: str, host: str = 'localhost', port: int = 5432):
        """
        Инициализация подключения к PostgreSQL
        
        :param database: Название базы данных
        :param user: Имя пользователя
        :param password: Пароль
        :param host: Хост (по умолчанию localhost)
        :param port: Порт (по умолчанию 5432)
        """
        self.conn_params = {
            'database': database,
            'user': user,
            'password': password,
            'host': host,
            'port': port
        }
        self.connection = None
        self.cursor = None

    def connect(self) -> None:
        """Установить соединение с базой данных"""
        try:
            self.connection = psycopg2.connect(**self.conn_params)
            self.cursor = self.connection.cursor(cursor_factory=RealDictCursor)
        except Exception as e:
            raise Exception(f"Ошибка подключения к базе данных: {str(e)}")

    def disconnect(self) -> None:
        """Закрыть соединение с базой данных"""
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

    def execute(self, query: str, params: Optional[tuple] = None) -> None:
        """
        Выполнить SQL запрос
        
        :param query: SQL запрос
        :param params: Параметры запроса (опционально)
        """
        if not self.connection or self.connection.closed:
            self.connect()
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
        except Exception as e:
            self.connection.rollback()
            raise Exception(f"Ошибка выполнения запроса: {str(e)}")

    def fetch_all(self, query: str, params: Optional[tuple] = None) -> List[Dict[str, Any]]:
        """
        Получить все строки результата запроса
        
        :param query: SQL запрос
        :param params: Параметры запроса (опционально)
        :return: Список словарей с результатами
        """
        if not self.connection or self.connection.closed:
            self.connect()
        try:
            self.cursor.execute(query, params)
            return self.cursor.fetchall()
        except Exception as e:
            raise Exception(f"Ошибка получения данных: {str(e)}")

    def fetch_one(self, query: str, params: Optional[tuple] = None) -> Optional[Dict[str, Any]]:
        """
        Получить одну строку результата запроса
        
        :param query: SQL запрос
        :param params: Параметры запроса (опционально)
        :return: Словарь с результатом или None
        """
        if not self.connection or self.connection.closed:
            self.connect()
        try:
            self.cursor.execute(query, params)
            return self.cursor.fetchone()
        except Exception as e:
            raise Exception(f"Ошибка получения данных: {str(e)}")

    def __enter__(self):
        """Поддержка контекстного менеджера"""
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Закрытие соединения при выходе из контекстного менеджера"""
        self.disconnect() 