import pytest
from api import PetFriends
from settings import valid_email, valid_password
from datetime import datetime
import sys

pf = PetFriends()

@pytest.fixture(autouse=True)
def get_api_key():
    """ Проверяем, что запрос api-ключа возвращает статус 200 и
    в результате содержится слово key"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status,
    # а текст ответа в result
    status, pytest.key, response_headers = pf.get_api_key(valid_email,
                                                          valid_password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert 'key' in pytest.key


@pytest.fixture(autouse=True)
def log_function(request):
    """Фикстура выводит на экран детализацию выполенния
       для каждого теста."""
    start_time = datetime.now()
    yield
    print('\n=========================================================')
    print(f'Test name: {request.function.__name__}')
    print(f'Start of test: {start_time}')
    print(request.module.__name__)
    print(request.fixturename)
    print(request.scope)
    print(request.cls)
    print(request.fspath)
    end_time = datetime.now()
    print ('==========================================================')
    print(f'End of test: {end_time}')
    print(f"Test duration: {end_time - start_time}")
    print ('==========================================================\n')


minversion = pytest.mark.skipif(
    sys.version_info < (3, 6), reason="at least mymodule-1.1 required"
)


