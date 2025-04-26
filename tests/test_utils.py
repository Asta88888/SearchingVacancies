import pytest
from src.utils import get_top_vacancies, filter_vacancies_by_salary_range, print_vacancies
from src.vacancies import Vacancies


def test_get_top_vacancies(vacancies_objects):
    top = get_top_vacancies(vacancies_objects, 2)
    assert len(top) == 2
    salaries = [vac.get_min_salary() for vac in top]
    assert salaries == sorted(salaries, reverse=True)


def test_filter_vacancies_by_salary_range(vacancies_objects):
    filtered = filter_vacancies_by_salary_range(vacancies_objects, 60000, 120000)
    for vac in filtered:
        salary = vac.get_min_salary()
        assert 60000 <= salary <= 120000
        filtered_empty = filter_vacancies_by_salary_range(vacancies_objects, 200000, 300000)
        assert filtered_empty == []


def test_print_vacancies(capsys, vacancies_objects):
    print_vacancies(vacancies_objects[:2])
    captured = capsys.readouterr()
    for vac in vacancies_objects[:2]:
        assert vac.name in captured.out