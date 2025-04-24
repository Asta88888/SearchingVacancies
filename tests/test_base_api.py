import pytest
from src.base_api import BaseApi


def test_base_api_instantiation_raises():
    with pytest.raises(TypeError):
        BaseApi()