import os.path
import shutil
import tempfile
import pytest
from src.api import HeadHunterApi
from src.save_info_to_json import SaveInfoToJson


@pytest.fixture
def hh_api():
    return HeadHunterApi()


@pytest.fixture
def temp_json_storage():
    temp_dir = tempfile.mkdtemp()
    file_name = "test_vacancies.json"
    full_path = os.path.join(temp_dir, file_name)
    storage = SaveInfoToJson(file_name=full_path)
    yield storage
    shutil.rmtree(temp_dir)


@pytest.fixture
def single_vacancy():
    return {
        "name": "Python разработчик",
        "url": "https://hh.ru/vacancy/119631518",
        "salary": 100000,
        "description": "Открытая"
    }


@pytest.fixture
def multiple_vacancies():
    return [
        {
            "name": "Java разработчик",
            "url": "https://hh.ru/vacancy/119631518",
            "salary": 50000,
            "description": "Открытая"
        },
        {
            "name": "SQL разработчик",
            "url": "https://hh.ru/vacancy/119631518",
            "salary": 100000,
            "description": "Открытая"
        }
    ]
