from typing import Any, Union


class Vacancies:
    """Класс для представления вакансии с полями: название, ссылка, зарплата и описание"""
    __slots__ = ("name", "link", "salary", "description")


    def __init__(self, name, link, salary, description):
        """Конструктор экземпляра вакансии"""
        self.name = name
        self.link = link
        self.salary = self.validate_salary(salary)
        self.description = description


    def __str__(self):
        """Возвращает строковое представление вакансии"""
        return f"{self.name} - {self.salary}₽\n{self.description}\n{self.link}"


    def validate_salary(self, salary: Any) -> Union[int, float, str]:
        """Валидация значения зарплаты"""
        if isinstance(salary, dict):
            return salary.get("from") or salary.get("to") or "Зарплата не указана"
        if isinstance(salary, (int, float)):
            return salary
        return "Зарплата не указана"


    def salary_comparison(self, other):
        """Сравнивает зарплату текущей вакансии с другой"""
        if isinstance(self.salary, (int, float)) and isinstance(other.salary, (int, float)):
            if self.salary > other.salary:
                print(f"Зарплата у {self.name} больше, чем у {other.name}")
            elif self.salary < other.salary:
                print(f"Зарплата у {self.name} меньше, чем у {other.name}")
            else:
                print(f"Зарплата у {self.name} и у {other.name} одинакова")
        else:
            print(f"Сравнение невозможно: у одной из вакансий не указана зарплата.")

    @staticmethod
    def sorted_vacancies_by_salary(vacancy_list):
        """Возвращает отсортированный список вакансий по убыванию зарплаты"""
        int_or_float_only = [v for v in vacancy_list if isinstance(v.salary, (int, float))]
        sorted_vacancies = sorted(int_or_float_only, key=lambda x: x.salary, reverse=True)
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
