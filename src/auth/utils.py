from passlib.context import CryptContext  # type: ignore

from config.settings import get_settings

_settings = get_settings()


pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def get_password_hash(password: str, salt: str) -> str:
    """
    Generate a password hash using the provided password.

    Args:
        password (str): The password to be hashed.
        salt (Optional[str]): Optional salt value for hashing. Defaults to None.

    Returns:
        str: The hashed password.
    """

    new_text = f'{_settings.secret_key}{password}{salt}'
    password_hashed: str = pwd_context.hash(new_text)

    return password_hashed


def verify_password(plain_password: str, salt: str, hashed_password: str) -> bool:
    """
    Verify the provided password against the hashed password.

    Args:
        plain_password (str): The plain text password.
        hashed_password (str): The hashed password.
        salt (Optional[str]): Optional salt value for hashing. Defaults to None.

    Returns:
        bool: True if the password matches, False otherwise.
    """

    new_text = f'{_settings.secret_key}{plain_password}{salt}'

    check_password: bool = pwd_context.verify(new_text, hashed_password)

    return check_password
