"""Старый файл, для работы необходимо подключить фикстуру get_key"""

import pytest
from api import PetFriends
from settings import valid_email, valid_password
from settings import invalid_email, invalid_password
import os

pf = PetFriends()


class TestClassPetFriends:
    """Class has scenery:
     - add pet (full = info + photo)
     - add pet (simple = info)
     - add pet (photo)"""

    @pytest.mark.api
    @pytest.mark.event
    def test_add_new_pet_with_valid_data(self, get_key,
                                         name = 'Sharik',
                                         animal_type = 'dvorterier',
                                         age = '4',
                                         pet_photo = 'images/dog01.jpg'):
        """Проверяем что можно добавить питомца с корректными данными
        инфо и фото"""


        # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
        pet_photo = os.path.join (os.path.dirname (__file__), pet_photo)
        # Добавляем питомца
        status, result, response_headers = \
            pf.add_new_pet(get_key, name, animal_type, age, pet_photo)
        # Сверяем полученный ответ с ожидаемым результатом
        assert status == 200, "Request hasn't executed successfully"
        assert result['name'] == name


    def test_add_new_pet_simple_valid_data(self, get_key,
                                           name='Барсик',
                                           animal_type='дворокот',
                                           age='6'):
        """Проверяем, что можно добавить питомца без фото с корректными
        данными"""

        # Добавляем питомца
        status, result, response_headers \
            = pf.add_new_pet_simple (get_key, name, animal_type, age)

        # Сверяем полученный ответ с ожидаемым результатом
        assert status == 200
        assert result['name'] == name
        assert result['pet_photo'] is ''


    def test_add_pet_photo_valid_data(self,
                                      get_key,
                                      pet_photo='images/cat1.jpg'):
        """Проверяем возможность добавления/замены фото
        существующему питомцу. Если список питомцев пустой, то добавляем
        питомца без фото"""


        _, my_pets, response_headers = pf.get_list_of_pets(get_key, "my_pets")

        pet_photo = os.path.join(os.path.dirname (__file__), pet_photo)

        # Если список пустой, то пробуем вначале добавляем нового питомца
        # и получаем список заново
        if len(my_pets['pets']) == 0:
            pf.add_new_pet_simple (get_key, "Барсик", "жук", "4")
            _, my_pets, response_headers = pf.get_list_of_pets (get_key, "my_pets")

        # Берём id первого питомца из списка и отправляем запрос на
        # добавление фотографии
        status, result, response_headers\
            = pf.add_pet_photo(get_key, my_pets['pets'][0]['id'], pet_photo)
        # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
        assert status == 200
        assert 'pet_photo' in result
