import os
import json


def test_init_creates_file_and_folder(temp_json_storage):
    assert os.path.exists(temp_json_storage.file_path)

    with open(temp_json_storage.file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        assert isinstance(data, list)
        assert data == []


def test_add_single_vacancy(temp_json_storage, single_vacancy):
    temp_json_storage.add_vacancies(single_vacancy)
    loaded = temp_json_storage.load()
    assert len(loaded) == 1
    assert loaded[0]["name"] == "Python разработчик"
    assert "id" in loaded[0]


def test_add_multiple_vacancies(temp_json_storage, multiple_vacancies):
    temp_json_storage.add_vacancies(multiple_vacancies)
    loaded = temp_json_storage.load()
    assert len(loaded) == 2
    for vacancy in loaded:
        assert "id" in vacancy


def test_get_vacancy(temp_json_storage, multiple_vacancies):
    temp_json_storage.add_vacancies(multiple_vacancies)
    filtered = temp_json_storage.get_vacancies(name="SQL разработчик")
    assert len(filtered) == 1
    assert filtered[0]["name"] == "SQL разработчик"


def test_delete_vacancy(temp_json_storage, single_vacancy):
    temp_json_storage.add_vacancies(single_vacancy)
    loaded = temp_json_storage.load()
    vacancy_id = loaded[0]["id"]
    temp_json_storage.delete_vacancies(vacancy_id)
    after_delete = temp_json_storage.load()
    assert len(after_delete) == 0


def test_clear_storage(temp_json_storage, multiple_vacancies):
    temp_json_storage.add_vacancies(multiple_vacancies)
    temp_json_storage.clear_storage()
    assert temp_json_storage.load() == []
