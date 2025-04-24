import pytest
from src.api import HeadHunterApi


@pytest.fixture
def hh_api():
    return HeadHunterApi()