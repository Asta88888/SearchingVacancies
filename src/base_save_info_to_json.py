from abc import ABC, abstractmethod


class BaseSaverToJson(ABC):
    """Абстрактный базовый класс для работы с хранилищами вакансий"""


    @abstractmethod
    def add_vacancies(self, vacancy):
        """Добавляет новую вакансию в хранилище"""
        pass


    @abstractmethod
    def get_vacancies(self, **kwargs):
        """Получает список вакансий, соответствующих переданным критериям"""
        pass


    @abstractmethod
    def delete_vacancies(self, vacancy_id):
        """Удаляет вакансию по её уникальному идентификатору"""
        pass


    def clear_storage(self):
        """Очищает хранилище вакансий. Заглушка. Пригодится для интеграции к БД"""
        pass