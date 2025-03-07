import csv
import sqlite3
from typing import List, Dict, Union

class FileToDB:
    def __init__(self, db_name: str = "database.db"):
        """
        Инициализация библиотеки.
        :param db_name: Имя файла базы данных SQLite.
        """
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def read_csv(self, file_path: str) -> List[Dict[str, Union[str, int, float]]]:
        """
        Чтение данных из CSV-файла.
        :param file_path: Путь к CSV-файлу.
        :return: Список словарей, где каждый словарь представляет строку из файла.
        """
        data = []
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
        return data

    def read_txt(self, file_path: str, delimiter: str = ",") -> List[Dict[str, Union[str, int, float]]]:
        """
        Чтение данных из TXT-файла.
        :param file_path: Путь к TXT-файлу.
        :param delimiter: Разделитель данных в файле (по умолчанию запятая).
        :return: Список словарей, где каждый словарь представляет строку из файла.
        """
        data = []
        with open(file_path, mode='r', encoding='utf-8') as file:
            headers = file.readline().strip().split(delimiter)
            for line in file:
                values = line.strip().split(delimiter)
                row = dict(zip(headers, values))
                data.append(row)
        return data

    def create_table(self, table_name: str, columns: List[str]):
        """
        Создание таблицы в базе данных.
        :param table_name: Имя таблицы.
        :param columns: Список колонок (например, ["id INTEGER PRIMARY KEY", "name TEXT", "age INTEGER"]).
        """
        columns_with_types = ", ".join(columns)
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_with_types})")
        self.conn.commit()

    def insert_data(self, table_name: str, data: List[Dict[str, Union[str, int, float]]]):
        if not data:
            raise ValueError("Данные для вставки отсутствуют.")

        columns = data[0].keys()
        columns_str = ", ".join(columns)
        placeholders = ", ".join(["?"] * len(columns))

        # Вставляем данные
        for row in data:
            values = [row[column] for column in columns]
            self.cursor.execute(f"INSERT INTO {table_name} ({columns_str}) VALUES ({placeholders})", values)
        self.conn.commit()

    def close(self):
        """
        Закрытие соединения с базой данных.
        """
        self.conn.close()

# Пример использования
if __name__ == "__main__":
    # Инициализация библиотеки
    file_to_db = FileToDB("example.db")

    # Чтение данных из CSV
    csv_data = file_to_db.read_csv("example.csv")
    print("Данные из CSV:", csv_data)

    # Чтение данных из TXT
    txt_data = file_to_db.read_txt("example.txt")
    print("Данные из TXT:", txt_data)

    # Создание таблицы
    file_to_db.create_table("users", ["id INTEGER PRIMARY KEY", "name TEXT", "age INTEGER"])

    # Вставка данных из CSV в таблицу
    file_to_db.insert_data("users", csv_data)

    # Вставка данных из TXT в таблицу
    file_to_db.insert_data("users", txt_data)

    # Закрытие соединения
    file_to_db.close()