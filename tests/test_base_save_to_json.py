import pytest
from src.base_save_info_to_json import BaseSaverToJson


def test_base_saver_to_json_instantiation_raises():
    with pytest.raises(TypeError):
        BaseSaverToJson()