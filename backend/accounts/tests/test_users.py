# accounts/tests.py
# from django.test import TestCase
import pytest

# from backend.accounts.models import User

# pytestmark = pytest.mark.django_db


# @pytest.fixture
# def normal_user(db):
#     user = User.objects.create_user(
#         email='admin@email.com',
#         password='demodemo',
#         first_name='Admin',
#         last_name='Admin',
#     )
#     return user


# @pytest.mark.django_db
# class TestUsers:
#     pytestmark = pytest.mark.django_db


#     def test_user_exists(self):
#         assert self.user.id_exists

#     def test_str(self):
#         assert self.user.email == 'admin@email.com'

#     def test_return_attributes(self):
#         fields = (
#             'id',
#             'email',
#             'first_name',
#             'last_name',
#             'password',
#             'is_active',
#             'is_admin',
#             'is_superuser',
#             'date_joined',
#             'last_login',
#         )

#         for field in fields:
#             with self.subTest():
#                 self.assertTrue(hasattr(User, field))

#     def test_user_is_authenticated(self):
#         assert self.user.is_authenticated

#     def test_user_is_active(self):
#         assert self.user.is_active

#     def test_user_is_staff(self):
#         assert self.user.is_staff

#     def test_user_is_superuser(self):
#         assert self.user.is_superuser

#     def test_superuser_is_superuser(self):
#         assert self.superuser.is_superuser

#     def test_user_has_perm(self):
#         assert self.user.has_perm

#     def test_user_has_module_perms(self):
#          assert self.user.has_module_perms

#     def test_user_get_full_name(self):
#         self.assertEqual(self.user.get_full_name(), 'Admin Admin')

#     def test_user_get_short_name(self):
#         self.assertEqual(self.user.get_short_name(), 'Admin')


@pytest.mark.django_db
def test_new_user(user_factory):
    user = user_factory.create()
    assert user.email == 'plautz@admin.com'


@pytest.mark.django_db
def test_return_attributes(user_factory):
    user = user_factory.create()
    print(user_factory.first_name, user_factory.email, user_factory.is_active)
    fields = (
        user.email,
        user.first_name,
        user.is_admin,
        user.is_active,
    )

    for field in fields:
        assert user, field
