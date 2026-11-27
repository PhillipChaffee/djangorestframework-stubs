from typing import assert_type

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


# case: token_user
def token_user(token: Token) -> None:
    # The mypy plugin resolves `_User` to `AUTH_USER_MODEL`; other type checkers see `AbstractBaseUser`.
    assert_type(token.user, User)  # pyright: ignore[reportAssertTypeFailure]
    assert_type(token.user, AbstractBaseUser)  # type: ignore[assert-type]
