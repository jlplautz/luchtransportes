import pytest

from backend.accounts.models import User


@pytest.fixture
def normal_user(db):
    user = User.objects.create_user(
        'plautz@admin.com',
        'Jorge',
    )
    return user


def test_normal_user_created(normal_user):
    assert normal_user.is_active
    assert normal_user.email == 'plautz@admin.com'
    assert normal_user.first_name == ''
