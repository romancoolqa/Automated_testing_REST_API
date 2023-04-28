import pytest
from api import PetFriends
from settings import generate_string, russian_chars
from settings import chinese_chars, special_chars

pf = PetFriends()

@pytest.mark.parametrize("filter", [
    generate_string(255),
    generate_string(1001),
    russian_chars(),
    russian_chars().upper(),
    chinese_chars(),
    special_chars(), 123],
                         ids =
                        ['255 symbols',
                         'more than 1000 symbols',
                         'russian',
                         'RUSSIAN',
                         'chinese',
                         'specials',
                         'digit'])
def test_get_all_pets_with_negative_filter(filter):
    ''' Получение питомца с заданным фильтром - негативный тест. '''

    pytest.status, result, response_headers = \
       pf.get_list_of_pets(pytest.key, filter)

    # Проверяем статус ответа
    assert pytest.status == 400