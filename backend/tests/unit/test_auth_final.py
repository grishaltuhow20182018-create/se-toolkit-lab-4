import pytest
from fastapi import HTTPException
from app.auth import verify_api_key
from unittest.mock import MagicMock, patch

def create_creds(token: str):
    creds = MagicMock()
    creds.credentials = token
    return creds

# --- AI-GENERATED & CURATED TESTS ---

def test_keep_wrong_key():
    """[KEEP] Проверка неверного ключа."""
    with patch("app.auth.settings.api_key", "valid_key"):
        with pytest.raises(HTTPException) as exc:
            verify_api_key(create_creds("wrong"))
        assert exc.value.status_code == 401

def test_keep_empty_key():
    """[KEEP] Проверка пустого ввода."""
    with patch("app.auth.settings.api_key", "valid_key"):
        with pytest.raises(HTTPException) as exc:
            verify_api_key(create_creds(""))
        assert exc.value.status_code == 401

def test_fix_case_sensitivity():
    """[FIXED] Был код 404, исправлен на 401."""
    with patch("app.auth.settings.api_key", "SECRET"):
        with pytest.raises(HTTPException) as exc:
            verify_api_key(create_creds("secret"))
        assert exc.value.status_code == 401

def test_fix_return_value():
    """[FIXED] Исправлено ожидаемое возвращаемое значение."""
    with patch("app.auth.settings.api_key", "token123"):
        result = verify_api_key(create_creds("token123"))
        assert result == "token123"

# [DISCARDED] Тест на базу данных удален из кода.
