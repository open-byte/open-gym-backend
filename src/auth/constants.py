from user.models.general import User

JWT_ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

AUTH_MODEL = User

__all__ = [
    'JWT_ALGORITHM',
    'ACCESS_TOKEN_EXPIRE_MINUTES',
    'AUTH_MODEL',
]
