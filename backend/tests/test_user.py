def test_new_user_name(new_user):
    assert new_user.first_name == 'Jorge'


def test_new_user_cpf(new_user):
    assert new_user.last_name == 'Plautz'


def test_new_user_email(new_user):
    assert new_user.email == 'plautz@email.com'


def test_new_user_status(new_user):
    assert new_user.is_active == True
