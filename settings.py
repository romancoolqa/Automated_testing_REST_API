
import os
from dotenv import load_dotenv
import functools
import json
from datetime import datetime


load_dotenv()

valid_email = os.getenv('valid_email')
valid_password = os.getenv('valid_password')
invalid_email = os.getenv('invalid_email')
invalid_password = os.getenv('invalid_password')
BASE_URL = 'https://petfriends.skillfactory.ru/'

def generate_string(n):
    return "x" * n

def russian_chars():
    return 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

def english_chars():
    return 'abcdefghijklmnopqrstuvwxyz'

# Здесь взял 20 популярных китайских иероглифов
def chinese_chars():
    return '的一是不了人我在有他这为之大来以个中上们'

def special_chars():
    return '|\\/!@#$%^&*()-_=+`~?"№;:[]{}'

def is_age_valid(age):
   # Проверяем, что возраст - это число от 1 до 49 и целое
   return age.isdigit() and 0 < int(age) < 50 and float(age) == int(age)


def log_api_request(func):
    """Декоратор, который логирует запросы в API тестах"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        value = func(*args, **kwargs)
        # Записываем полученные ответы в файл log.txt:
        log_txt = "log_" + func.__name__ + ".txt"
        with open(log_txt, 'a', encoding='utf8') as my_file:
            my_file.write(f'\nName Func: {func.__name__}\n'
                          f'Start time: {start_time}\n'
                          f'Headers of query: {value[2]["Headers of query"]}\n'
                          f'Path parametrs: {value[2]["Path parametrs"]}\n'
                          f'Query parametrs: {value[2]["Query parametrs"]}\n'
                          f'Query body: {value[2]["Query body"]}\n'
                          f'Content: {value[2]["Content"]}\n'
                          f'Optional: {value[2]["Optional"]}\n'
                          f'URL: {value[2]["URL"]}\n'
                          f'Path URL: {value[2]["Path URL"]}\n'
                          f'Cookie: {value[2]["Cookie"]}\n'
                          f'End time: {datetime.now()}\n'
                          f'================================================\n'
                          f'Response status: {value[0]}\n'
                          f'Response body:\n')
            json.dump(value[1], my_file, ensure_ascii=False, indent=4)

        return value[0], value[1], value[2]["Content"]
    return wrapper