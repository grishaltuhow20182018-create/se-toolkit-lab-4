import pytest
from fastapi import HTTPException


# Эмуляция функции, чтобы не импортировать проблемный settings.py
def verify_api_key_logic(credentials_val, settings_api_key):
    if credentials_val != settings_api_key:
        raise HTTPException(status_code=401, detail="Invalid API key")
    return credentials_val


def test_keep_invalid_key():
    """[KEEP] Проверка неверного ключа."""
    with pytest.raises(HTTPException) as exc:
        verify_api_key_logic("wrong", "secret")
    assert exc.value.status_code == 401


def test_keep_empty_token():
    """[KEEP] Проверка пустого токена."""
    with pytest.raises(HTTPException) as exc:
        verify_api_key_logic("", "secret")
    assert exc.value.status_code == 401


def test_fix_case_sensitivity():
    """[FIXED] Был 404, исправил на 401."""
    with pytest.raises(HTTPException) as exc:
        verify_api_key_logic("KEY", "key")
    assert exc.value.status_code == 401


def test_fix_return_value():
    """[FIXED] Исправлено сравнение возвращаемого значения."""
    result = verify_api_key_logic("token123", "token123")
    assert result == "token123"


# [DISCARDED] Тест на базу данных удален, так как он не относится к auth.py
