import json
import os
from uuid import uuid4
from src.base_save_info_to_json import BaseSaverToJson


class SaveInfoToJson(BaseSaverToJson):
    """Класс для работы с JSON-файлом, сохраняет, удаляет, фильтрует вакансии"""


    def __init__(self, file_name="vacancies.json"):
        """Конструктор объекта, создает папку или файл, если ранее не созданы"""
        self.file_path = os.path.join("../data", file_name)
        if not os.path.exists("../data"):
            os.makedirs("../data")
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w", encoding="utf-8") as f:
                json.dump([], f)


    def load(self):
        """Загружает данные из JSON-файла"""
        with open(self.file_path, "r", encoding="utf-8") as f:
            return json.load(f)


    def save(self, data):
        """Сохраняет данные в JSON-файл"""
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)


    def add_vacancies(self, vacancies):
        """Добавляет одну или несколько вакансий в файл с генерацией уникального идентификатора"""
        data = self.load()
        if isinstance(vacancies, list):
            for vacancy in vacancies:
                vacancy["id"] = str(uuid4())
                data.append(vacancy)
        else:
            vacancies["id"] = str(uuid4())
            data.append(vacancies)
        self.save(data)


    def get_vacancies(self, **key_words):
        """Получает вакансии по заданным критериям"""
        data = self.load()
        filtered = data
        for key, value in key_words.items():
            filtered = [v for v in filtered if v.get(key) == value]
        return filtered


    def delete_vacancies(self, vacancy_id: str):
        """Удаляет вакансию по ID"""
        data = self.load()
        updated = [v for v in data if v.get("id") != vacancy_id]
        self.save(updated)


    def clear_storage(self):
        """Очистить весь файл."""
        self.save([])


if __name__ == "__main__":
    storage = SaveInfoToJson()

    vacancy_data = {
        "name": "Data Scientist",
        "url": "https://hh.ru/vacancy/119631518",
        "salary": "150000",
        "description": "Открытая"
    }
    vacancy_data1 = {
        "name": "Python разработчик",
        "url": "https://hh.ru/vacancy/119631518",
        "salary": 100000,
        "description": "Открытая"
    }
    vacancy_data2 = {
        "name": "Java разработчик",
        "url": "https://hh.ru/vacancy/119631518",
        "salary": 50000,
        "description": "Открытая"
    }
    vacancy_data3 = {
        "name": "SQL разработчик",
        "url": "https://hh.ru/vacancy/119631518",
        "salary": 100000,
        "description": "Открытая"
    }

    storage.add_vacancies(vacancy_data)
    storage.add_vacancies(vacancy_data1)
    storage.add_vacancies(vacancy_data2)
    storage.add_vacancies(vacancy_data3)


    found = storage.get_vacancies(name="SQL разработчик")
    print(f"Найдено {len(found)} вакансий:\n", found)


    # storage.delete_vacancies("341b3998-a0e7-4712-84f4-ecd353bed2c8")
    # storage.clear_storage()
