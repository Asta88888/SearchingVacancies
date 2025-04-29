from abc import ABC, abstractmethod
from typing import Any


class BaseApi(ABC):
    """Абстрактный класс для работы с API сервиса с вакансиями"""


    @abstractmethod
    def get_connect(self, params: dict) -> Any:
        """Устанавливает подключение к API"""
        pass


    @abstractmethod
    def get_vacancies(self, keyword: str) -> Any:
        """Получает список вакансий по ключевому слову"""
        pass



