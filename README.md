Автоматизированное тестирование REST API сервисов социальной сети любителей домашних животных [PetFriends](https://petfriends.skillfactory.ru/). 
-
Цель: изучение и приобретение навыков тестирования REST API при помощи [Python]() - библиотеки requests и pytest. Работа с API документацией - [Swagger](https://petfriends.skillfactory.ru/apidocs/#/). Описание задания в файле `TASK.md`

Как запускать тесты:
-
1) Установить все зависимости:
В командной строке терминала (bash) набрать и выполнить: 
pip install -r requirements.txt
2) Скачать Selenium WebDriver: https://chromedriver.chromium.org/downloads (выбрать совместимую версию с вашим браузером Chrome).
3) Запуск тестов:
python -m pytest -v --driver Chrome --driver-path ~/chrome tests/*
Пример:
python -m pytest -v --driver Chrome --driver-path D:/chromedriver_win32/chromedriver.exe tests/test_get_all_pets_positive.py

☝️ Пароли спрятаны в файл .env (не выложен здесь).\
Создать в директории проекта файл .env, в него записать  
valid_email = "ваша учетная запись"\
valid_password = "ваш пароль"\
invalid_email = "хххх"\
invalid_password = "qwerty"\