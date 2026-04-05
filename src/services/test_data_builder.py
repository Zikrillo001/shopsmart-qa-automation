from src.utils.helpers import generate_random_email, generate_random_string


class TestDataBuilder:
    @staticmethod
    def build_user_payload() -> dict:
        return {
            "name": generate_random_string(10),
            "email": generate_random_email(),
            "password": "Password123!",
        }

    @staticmethod
    def build_login_payload(email: str, password: str) -> dict:
        return {
            "email": email,
            "password": password,
        }