from typing import NoReturn, final


def hello_world():
    """Just print `Hello from Rust!`"""


class UserGotAngryException(Exception): ...


@final
class User:
    def __init__(self, name: str, age: int):...

    def greet(self) -> None:
        """Just print a greeting from user."""
    
    def get_age(self) -> int: ...

    def raise_angry(self) -> NoReturn:
        """raise a UserAngryException"""
