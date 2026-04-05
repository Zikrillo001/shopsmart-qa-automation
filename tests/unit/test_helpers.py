from src.utils.helpers import (
    build_headers,
    generate_random_email,
    generate_random_string,
    is_not_empty,
)


def test_is_not_empty_returns_true_for_valid_value():
    assert is_not_empty("hello") is True


def test_is_not_empty_returns_false_for_empty_string():
    assert is_not_empty("") is False


def test_generate_random_email_returns_example_email():
    email = generate_random_email()
    assert "@example.com" in email
    assert "testuser_" in email


def test_generate_random_string_returns_correct_length():
    value = generate_random_string(12)
    assert len(value) == 12


def test_build_headers_without_token():
    headers = build_headers()
    assert headers["Content-Type"] == "application/json"
    assert "Authorization" not in headers


def test_build_headers_with_token():
    headers = build_headers("abc123")
    assert headers["Authorization"] == "Bearer abc123"