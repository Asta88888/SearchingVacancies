import re
from typing import Any, Union


class Vacancies:
    """Класс для представления вакансии с полями: название, ссылка, зарплата и описание"""
    __slots__ = ("name", "url", "salary", "description")


    def __init__(self, name, url, salary, description):
        """Конструктор экземпляра вакансии"""
        self.name = name
        self.url = url
        self.salary = self.validate_salary(salary)
        self.description = description


    def __str__(self):
        """Возвращает строковое представление вакансии"""
        salary_str = f"{self.salary}₽" if self.salary is not None else "Зарплата не указана"
        return f"{self.name} - {salary_str}\n{self.description}\n{self.url}"


    def to_dict(self):
        return {
            "name": self.name,
            "url": self.url,
            "salary": self.salary if self.salary is not None else "Зарплата не указана",
            "description": self.description,
        }


    def validate_salary(self, salary: Any) -> Union[int, float, str, None]:
        """Валидация значения зарплаты"""
        if isinstance(salary, dict):
            # Ожидаем словарь с ключами "from" и "to"
            min_salary = salary.get("from")
            max_salary = salary.get("to")
            if min_salary is not None:
                return int(min_salary)
            elif max_salary is not None:
                return int(max_salary)
            else:
                return None
        if isinstance(salary, (int, float)):
            return salary
        if isinstance(salary, str):
            # Попытка извлечь минимальное число из строки типа "100 000-150 000 руб."
            nums = re.findall(r'\d+', salary.replace(" ", ""))
            if nums:
                return int(nums[0])
            else:
                return None
        return None


    def get_min_salary(self) -> Union[int, float, None]:
        """Возвращает минимальную числовую зарплату или None"""
        if isinstance(self.salary, (int, float)):
            return self.salary
        # Если зарплата — строка, пытаемся извлечь число
        if isinstance(self.salary, str):
            nums = re.findall(r'\d+', self.salary.replace(" ", ""))
            if nums:
                return int(nums[0])
        return None


    def salary_comparison(self, other):
        """Сравнивает зарплату текущей вакансии с другой"""
        self_salary = self.get_min_salary()
        other_salary = other.get_min_salary()

        if self_salary is not None and other_salary is not None:
            if self_salary > other_salary:
                print(f"Зарплата у {self.name} больше, чем у {other.name}")
            elif self_salary < other_salary:
                print(f"Зарплата у {self.name} меньше, чем у {other.name}")
            else:
                print(f"Зарплата у {self.name} и у {other.name} одинакова")
        else:
            print(f"Сравнение невозможно: у одной из вакансий не указана зарплата.")


    @staticmethod
    def sorted_vacancies_by_salary(vacancy_list):
        """Возвращает отсортированный список вакансий по убыванию минимальной зарплаты"""
        filtered = [v for v in vacancy_list if v.get_min_salary() is not None]
        sorted_vacancies = sorted(filtered, key=lambda x: x.get_min_salary(), reverse=True)
        return sorted_vacancies


if __name__ == "__main__":
    v1 = Vacancies("Python разработчик", "https://hh.ru/vacancy/119631518", 100000, "Открытая")
    v2 = Vacancies("Java разработчик", "https://hh.ru/vacancy/119631518", 50000, "Открытая")
    v3 = Vacancies("SQL разработчик", "https://hh.ru/vacancy/119631518", 100000, "Открытая")
    v4 = Vacancies("Junior разработчик", "https://hh.ru/vacancy/119631518", None,"Открытая")

    print("---------")
    v1.salary_comparison(v2)
    v1.salary_comparison(v3)
    v1.salary_comparison(v4)
    print("---------")
    print(v1)
    print(v2)
    print(v3)
    print(v4)
    print("---------")
    vacancies = [v1, v2, v3, v4]
    sorted_vacancies = Vacancies.sorted_vacancies_by_salary(vacancies)
    print("\nОтсортированные вакансии:")
    for vacancy in sorted_vacancies:
        print(vacancy)
