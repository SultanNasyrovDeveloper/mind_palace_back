import pytest

from mind_palace.palace.models import UserMindPalace

from ..test_account.factories import UserFactory


@pytest.mark.django_db
def test_user_mind_palace_create():
    """
    Test that user mind palace created for every user creation.
    """
    user = UserFactory()
    assert (
        UserMindPalace.objects.filter(user=user).exists(),
        f'User mind palace was not created for new user: {user.id}'
    )