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
db_uuid = {"db_uuid": "0655bc53-db5b-7762-8000-4fe80aae1b4f"}
json_db_uuid = json.dumps(db_uuid)

sid = dict(result.cookies)
print(sid)
del_db = requests.post('https://dbend.areso.pro/db_delete', data=json_db_uuid, cookies=sid)
print(del_db.text)


# sid_del = result.cookies.get('sid')
# print(sid_del)


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

    @allure.sub_suite('DELETE')
    @allure.title('delete db')
    def test_delete_db(self):
        print('\n\nMethod DELETE: delete_db')
        result_post_db_list = API.delete_db('0655bc53-db5b-7762-8000-4fe80aae1b4f', sid)
        Checking.check_status_code(result_post_db_list, 200)

# body3 = {"dbtype": 3, "dbversion": 5, "env": 3, "region": 3}
# x = json.dumps(body3)
# print(sid)
# print(type(sid))
# result3 = requests.post('https://dbend.areso.pro/db_create', data=x, cookies=sid)
# print(result3.text)
