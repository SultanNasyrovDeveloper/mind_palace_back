import pytest

from .factories import UserFactory


@pytest.fixture
@pytest.mark.django_db
def user():
    return UserFactory()