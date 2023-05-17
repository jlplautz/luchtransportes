import pytest
from pytest_factoryboy import register

from backend.accounts.tests.factories import UserFactory

register(UserFactory)
