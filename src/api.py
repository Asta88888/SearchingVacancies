from src.base_api import BaseApi
import requests
from typing import Any

class HeadHunterApi(BaseApi):
    """Класс для работы с API платформы hh.ru"""

    def __init__(self):
        self._url = "https://api.hh.ru/vacancies"


    def _get_connect(self, params: dict):
        """Устанавливает подключение к API hh.ru"""
        try:
            response = requests.get(self._url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"Ошибка подключения: {e}")


    def get_connect(self, params:dict) -> Any:
        """Вызываем приватный метод подключения"""
        return self._get_connect(params)


    def get_vacancies(self, keyword: str):
        """Получает список вакансий по ключевому слову с платформы hh.ru"""
        params = {
            "text": keyword,
            "area": 113,
            "per_page": 100
        }
        try:
            data = self._get_connect(params)
            return data.get("items", [])
        except ConnectionError as e:
            print(f"Не удалось получить вакансии: {e}")
            return []


if __name__ == "__main__":
    hh = HeadHunterApi()
    vacancies = hh.get_vacancies("Python разработчик")
    print(vacancies)
