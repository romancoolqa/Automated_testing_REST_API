import pytest
from api import PetFriends


pf = PetFriends()

@pytest.mark.parametrize("filter",
                        ['', 'my_pets'],
                        ids=['empty string', 'only my pets'])
def test_get_all_pets_with_valid_key(filter):
    ''' Получение питомцев с заданным фильтром. '''

    pytest.status, result, response_headers = \
       pf.get_list_of_pets(pytest.key, filter)
    # Проверяем статус ответа
    assert pytest.status == 200
    assert len(result['pets']) > 0