import pytest
from api import PetFriends


pf = PetFriends()



@pytest.mark.parametrize('accept',
                        ['application/json',
                         'application/xml',
                         'multipart/form-data',
                         'text/html, charset=utf-8'],
ids = ['application/json',
       'application/xml',
       'multipart/form-data',
       'text/html, charset=utf-8'])
def test_successful_update_self_pet_info(accept, name='Barboskin',
                                         animal_type='dog',
                                         age=5):
    """Checking possibility of pets update"""

    # Получаем ключ auth_key посредством фикстуры

    # Получаем список своих питомцев
    _, my_pets, response_headers = pf.get_list_of_pets (pytest.key, "my_pets")

    # Еслди список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result, response_headers = pf.update_pet_info(pytest.key,
                                            my_pets['pets'][0]['id'],
                                            name, animal_type, age, accept)
        # Проверяем что статус ответа = 200 и имя питомца соответствует
        # заданному
        assert status == 200
        assert result['name'] == name
        assert response_headers['content-type'] == 'application/json' or \
               'application/xml'
    else:
        # если список питомцев пустой, то выкидываем исключение с текстом
        # об отсутствии своих питомцев
        raise Exception ("There is no my pets")