import re
from typing import Any, Union


class Vacancies:
    """Класс для представления вакансии с полями: название, ссылка, зарплата и описание"""
    __slots__ = ("name", "url", "salary", "description")


    def __init__(self, name, url, salary, description):
        """Конструктор экземпляра вакансии"""
        self.name = name
        self.url = url
        self.salary = self._validate_salary(salary)
        self.description = description


    def __str__(self):
        """Возвращает строковое представление вакансии"""
        salary_str = f"{self.salary}₽" if self.salary is not None else "Зарплата не указана"
        return f"{self.name} - {salary_str}\n{self.description}\n{self.url}"


    def cast_to_dict(self):
        return {
            "name": self.name,
            "url": self.url,
            "salary": self.salary if self.salary is not None else "Зарплата не указана",
            "description": self.description,
        }


    def _validate_salary(self, salary: Any) -> Union[int, float, str, None]:
        """Валидация значения зарплаты"""
        if isinstance(salary, dict):
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
        if isinstance(self.salary, str):
            nums = re.findall(r'\d+', self.salary.replace(" ", ""))
            if nums:
                return int(nums[0])
        return None


    def __lt__(self, other):
        if not isinstance(other, Vacancies):
            return NotImplemented
        return (self.get_min_salary() or 0) < (other.get_min_salary() or 0)


    def __gt__(self, other):
        if not isinstance(other, Vacancies):
            return NotImplemented
        return (self.get_min_salary() or 0) > (other.get_min_salary() or 0)


    def __eq__(self, other):
        if not isinstance(other, Vacancies):
            return NotImplemented
        return (self.get_min_salary() or 0) == (other.get_min_salary() or 0)


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
    print(v1>v2)

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
