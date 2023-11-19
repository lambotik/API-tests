import json
import os

import allure
import pytest
import requests

from utils.checking import Checking

from utils.request import API
from dotenv import load_dotenv

base_url = 'https://dbend.areso.pro'  # Base url
load_dotenv()
email = os.getenv('EMAIL')
password = os.getenv('PASSWORD')
body = {"email": f'{email}', "password": f'{password}'}

result = requests.post('https://dbend.areso.pro/login', json=body)

sid = dict(result.cookies)


@allure.epic('GET REQUESTS')
@allure.suite('REQUESTS GET')
class TestGET:
    @allure.sub_suite('GET')
    @allure.title('test tos')
    def test_tos(self):
        result_get = API.get_tos()
        Checking.check_status_code(result_get, 200)

    @allure.sub_suite('GET')
    @allure.title('List dbtypes')
    def test_list_dbtypes(self):
        result_get = API.get_list_dbtypes()
        Checking.check_status_code(result_get, 200)

    @allure.sub_suite('GET')
    @allure.title('List dbversions')
    def test_list_dbversions(self):
        result_get = API.get_list_dbversions()
        Checking.check_status_code(result_get, 200)

    @allure.sub_suite('GET')
    @allure.title('List envs')
    def test_list_envs(self):
        result_get = API.get_list_envs()
        Checking.check_status_code(result_get, 200)

    @allure.sub_suite('GET')
    @allure.title('List regions')
    def test_list_regions(self):
        result_get = API.get_list_regions()
        Checking.check_status_code(result_get, 200)


@allure.epic('POST REQUESTS')
@allure.suite('REQUESTS POST')
class TestPOST:
    @allure.sub_suite('POST')
    @allure.title('Post login')
    def test_post_login(self):
        print('\n\nMethod POST: login')
        result_post = API.post_login(body)
        status_code, sid = result_post
        Checking.check_status_code(status_code, 200)

    @allure.sub_suite('POST')
    @allure.title('Post db list')
    def test_post_db_list(self):
        print('\n\nMethod POST: db_list')
        result_post_db_list = API.post_db_list(sid)
        Checking.check_status_code(result_post_db_list, 200)

    @allure.sub_suite('POST')
    @allure.title('Post db create')
    def test_post_db_create(self):
        print('\n\nMethod POST: db_create')
        result_post_db_list = API.post_db_create(sid)
        Checking.check_status_code(result_post_db_list, 201)


result = requests.post('https://dbend.areso.pro/db_create', sid)
print(result.text)