import pytest
from api import PetFriends


pf = PetFriends()

# TEST - delete all pets filter='my_pets'

@pytest.mark.api
@pytest.mark.event
def test_delete_all(filter='my_pets'):
    """Check possibility of all pets deletion"""

    # filter = ''
    # Запрашиваем список своих питомцев
    _, my_pets, response_headers = pf.get_list_of_pets(pytest.key, filter)
    number_pets = len (my_pets['pets'])
    print(f"\n\nNumber of pets is {number_pets}\n")

    # Если список питомцев не ноль, то запуск цикла удаления
    while len (my_pets['pets']) > 1:
        for pet in range(len (my_pets['pets']) - 1):
                pf.delete_pet (pytest.key, my_pets['pets'][pet]['id'])
        _, my_pets, response_headers = pf.get_list_of_pets(pytest.key, filter)
    print (f'\nList of my_pets is empty!!\n')
    # Ещё раз запрашиваем список своих питомцев
    status, my_pets, response_headers = pf.get_list_of_pets(pytest.key, filter)

    # Проверяем что статус ответа равен 200
    assert status == 200
    assert len (my_pets['pets']) == 1