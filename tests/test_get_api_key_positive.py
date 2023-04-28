import pytest
from api import PetFriends
from settings import valid_email, valid_password


pf = PetFriends()

#    ТЕСТ ЗАПРОСА API KEY С ПОЗИТИВНЫМ СЦЕНАРИЕМ
@pytest.mark.api
@pytest.mark.auth
def test_get_api_key(email=valid_email, password=valid_password):
    """ Проверяем, что запрос api-ключа возвращает статус 200 и в
    результате содержится слово key"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status,
    # а текст ответа в auth_key
    status, auth_key, response_headers = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert 'key' in auth_key
