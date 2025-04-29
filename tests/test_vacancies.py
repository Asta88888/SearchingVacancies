import pytest
from src.vacancies import Vacancies


def test_sorted_vacancies_by_salary(sample_vacancies):
    v1, v2, v3, v4 = sample_vacancies
    vacancies = [v2, v4, v1, v3]
    sorted_result = Vacancies.sorted_vacancies_by_salary(vacancies)
    assert sorted_result == [v1, v3, v2] or sorted_result == [v3, v1, v2]
    assert all(v.get_min_salary() is not None for v in sorted_result)


@pytest.mark.parametrize("salary_input, expected", [
    (100000, 100000),
    ("120000", 120000),
    ("от 90 000", 90000),
    ({"from": 75000, "to": 95000}, 75000),
    ({"to": 95000}, 95000),
    ({"from": None, "to": None}, None),
    (None, None),
    ("Зарплата не указана", None),
    ]
)
def test_get_min_salary(salary_input, expected):
    vacancy = Vacancies("Тест вакансия", "https://hh.ru", salary_input, "Описание")
    assert vacancy.get_min_salary() == expected


@pytest.mark.parametrize("salary_input, expected", [
    (100000, 100000),
    (120000.5, 120000.5),
    ("130000", 130000),
    ("от 90 000 до 150000", 90000),
    ("нет данных", None),
    ({"from": 70000, "to": 95000}, 70000),
    ({"to": 95000}, 95000),
    ({"from": None, "to": None}, None),
    ([], None)
])
def test_validate_salary(salary_input, expected):
    vacancy = Vacancies("Тест", "https://hh.ru", salary_input, "Описание")
    assert vacancy.salary == expected


@pytest.mark.parametrize("salary_input, expected", [
    (100000, 100000),
    ("120000", 120000),
    (None, "Зарплата не указана"),
])
def test_to_dict(salary_input, expected):
    vacancy = Vacancies("Python разработчик", "https://hh.ru/vacancy/119631518", salary_input, "Открытая")
    result = vacancy.cast_to_dict()
    assert isinstance(result, dict)
    assert result["name"] == "Python разработчик"
    assert result["url"] == "https://hh.ru/vacancy/119631518"
    assert result["description"] == "Открытая"
    assert result["salary"] == expected


@pytest.mark.parametrize(
    "salary_input, expected",
    [
        (100000, "100000₽"),  # число
        ("120000", "120000₽"),  # строка
        (None, "Зарплата не указана"),  # None
    ]
)
def test_vacancy_str(salary_input, expected):
    name = "DevOps инженер"
    url = "https://hh.ru/vacancy/321"
    description = "Поддержка CI/CD"
    vacancy = Vacancies(name, url, salary_input, description)

    expected_output = f"{name} - {expected}\n{description}\n{url}"
    assert str(vacancy) == expected_output