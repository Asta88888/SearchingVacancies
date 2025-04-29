import pytest
from unittest.mock import patch, Mock
import requests


def test_get_connect_success(hh_api):
    mock_response = {"items": [{"name": "Python Developer"}]}

    with patch("requests.get") as mock_get:
        mock_get.return_value = Mock(status_code=200)
        mock_get.return_value.json.return_value = mock_response
        mock_get.return_value.raise_for_status = Mock()

        result = hh_api._get_connect({"text": "Python"})
        assert result == mock_response


def test_get_connect_failure(hh_api):
    with patch("requests.get") as mock_get:
        mock_get.side_effect = requests.exceptions.RequestException("Connection error")

        with pytest.raises(ConnectionError):
            hh_api._get_connect({"text": "Python"})


def test_get_vacancies_success(hh_api):
    fake_items = [{"name": "Pyton Developer"}, {"name": "Java Developer"}]

    with patch.object(hh_api, "_get_connect", return_value={"items": fake_items}):
        result = hh_api.get_vacancies("python")
        assert result == fake_items


def test_get_vacancies_connection_error(hh_api, capsys):
    with patch.object(hh_api, "_get_connect", side_effect=ConnectionError("No internet")):
        result = hh_api.get_vacancies("python")
        assert result == []

        captured = capsys.readouterr()
        assert "Не удалось получить вакансии" in captured.out
