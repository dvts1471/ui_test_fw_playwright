from dataclasses import dataclass


@dataclass
class LoginData:
    username: str = 'Admin'
    password: str = 'admin123'