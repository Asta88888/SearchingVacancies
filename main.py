from src.api import HeadHunterApi
from src.vacancies import Vacancies
from src.save_info_to_json import SaveInfoToJson
from src.utils import filter_vacancies_by_keyword, filter_vacancies_by_salary_range, get_top_vacancies, print_vacancies


def main():
    hh_api = HeadHunterApi()
    storage = SaveInfoToJson()

    hh_vacancies = hh_api.get_vacancies("Python")

    vacancies_list = [
        Vacancies(
            vac["name"],
            vac["url"],
            vac["salary"],
            vac.get("description", "")
        )
        for vac in hh_vacancies
    ]
    print("\nПример описания вакансий:")
    for vac in vacancies_list[:5]:
        print(f"{vac.name}: '{vac.description[:50]}...'")

    storage.add_vacancies([vac.to_dict() for vac in vacancies_list])

    filter_words = input("Введите ключевые слова для фильтрации вакансий").split()
    salary_range = input("Введите диапазон зарплат через тире").replace(" ", "")
    min_salary, max_salary = map(int, salary_range.split("-"))

    print(f"Всего вакансий с API: {len(vacancies_list)}")
    filtered_vacancies = filter_vacancies_by_keyword(vacancies_list, filter_words)
    print(f"Вакансий после фильтрации по ключевым словам: {len(filtered_vacancies)}")
    ranged_vacancies = filter_vacancies_by_salary_range(filtered_vacancies, min_salary, max_salary)
    print(f"Вакансий после фильтрации по зарплате: {len(ranged_vacancies)}")

    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    top_vacancies = get_top_vacancies(ranged_vacancies, top_n)
    if not top_vacancies:
        print("Вакансии не найдены по заданным критериям.")
    else:
        print_vacancies(top_vacancies)


if __name__ == "__main__":
    main()

