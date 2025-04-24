from src.vacancies import Vacancies


def filter_vacancies_by_keyword(vacancies, keywords):
    """Фильтрует вакансии по ключевым словам в названии или описании"""
    result = []
    for vac in vacancies:
        combined_text = (vac.name + " " + vac.description).lower()
        if any(word.lower() in combined_text for word in keywords):
            result.append(vac)
    return result


def get_top_vacancies(vacancies, top_n):
    """Возвращает топ-N вакансий по зарплате"""
    return Vacancies.sorted_vacancies_by_salary(vacancies)[:top_n]


def filter_vacancies_by_salary_range(vacancies, min_salary, max_salary):
    """Фильтрует вакансии по заданному диапазону зарплат"""
    filtered = []
    for vac in vacancies:
        salary_min = vac.get_min_salary()
        if salary_min is not None and min_salary <= salary_min <= max_salary:
            filtered.append(vac)
    return filtered


def print_vacancies(vacancies):
    """Печатает список вакансий"""
    for i, vac in enumerate(vacancies, start=1):
        print(f"\nВакансия {i}. {vac}")
