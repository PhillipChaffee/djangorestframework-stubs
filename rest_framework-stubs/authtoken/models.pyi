from typing import Any, ClassVar, Self

from django.contrib.auth.models import _User
from django.db import models
from django.db.models.manager import Manager

class Token(models.Model):
    key: models.CharField
    user: models.OneToOneField[_User, _User]
    created: models.DateTimeField
    objects: ClassVar[Manager[Self]]
    @classmethod
    def generate_key(cls) -> str: ...

class TokenProxyQuerySet(models.QuerySet["TokenProxy"]): ...

class TokenProxy(Token):
    # This is how drf defines this:
    @property  # type: ignore[no-redef]
    def pk(self) -> Any: ...  # type: ignore[override]
