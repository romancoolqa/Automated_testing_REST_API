import pytest
from api import PetFriends
from settings import valid_email, valid_password
from settings import invalid_email, invalid_password


pf = PetFriends()

#    ТЕСТЫ ЗАПРОСА API KEY С НЕГАТИВНЫМ СЦЕНАРИЕМ
@pytest.mark.parametrize("email", [
    '',
    valid_email,
    invalid_email],
                         ids=[
                             'empty',
                             'valid email',
                             'invalid email'])
@pytest.mark.parametrize("password", [
    '',
    invalid_password],
                         ids=[
                             'empty',
                             'invalid password'])
@pytest.mark.api
@pytest.mark.auth
def test_get_api_key(email, password):
    """ Проверяем, что запрос api-ключа возвращает статус 403"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status,
    # а текст ответа в auth_key
    status, auth_key, response_headers = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert 'key' not in auth_key
