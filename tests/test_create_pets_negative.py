import pytest
from api import PetFriends
from settings import russian_chars
from settings import chinese_chars, special_chars


pf = PetFriends()

@pytest.mark.parametrize("name", [''], ids=['empty'])
@pytest.mark.parametrize("animal_type", [''], ids=['empty'])
@pytest.mark.parametrize("age",
    ['', '-1', '0', '100', '1.5', '2147483647', '2147483648',
     special_chars(), russian_chars(), russian_chars().upper(),
     chinese_chars()],
    ids=['empty', 'negative', 'zero', 'greater than max', 'float',
         'int_max', 'int_max + 1', 'specials', 'russian', 'RUSSIAN',
         'chinese'])
def test_add_new_pet_simple_negative(name, animal_type, age):

   # Добавляем питомца
   pytest.status, result, response_headers\
       = pf.add_new_pet_simple(pytest.key, name, animal_type, age)

   # Сверяем полученный ответ с ожидаемым результатом
   assert pytest.status == 400