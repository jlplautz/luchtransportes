import factory
from faker import Faker

from backend.accounts.models import User

fake = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = 'Jorge'
    email = 'plautz@admin.com'
    is_admin = False
    is_active = False
