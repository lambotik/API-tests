import json

import allure
import mysql.connector

from utils.checking import Checking
from utils.config_my_sql import DataMySql
from utils.request import API


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
        result_post = API.post_login(DataMySql.body)
        status_code, sid = result_post
        Checking.check_status_code(status_code, 200)

    @allure.sub_suite('POST')
    @allure.title('Post db create')
    def test_post_db_create(self):
        print('\n\nMethod POST: db_create')
        result_post_db_list = API.post_db_create(DataMySql.sid)
        Checking.check_status_code(result_post_db_list, 201)

    @allure.sub_suite('POST')
    @allure.title('Post db list')
    def test_post_db_list(self):
        print('\n\nMethod POST: db_list')
        result_post_db_list = API.post_db_list(DataMySql.sid)
        Checking.check_status_code(result_post_db_list, 200)

    @allure.sub_suite('DELETE')
    @allure.title('delete db')
    def test_delete_db(self):
        print('\n\nMethod DELETE: delete_db')
        list_db = API.post_db_list(DataMySql.sid)
        json_list_db = json.loads(list_db.text)
        first_db_uuid = list(json_list_db['content'].keys())[0]
        result_post_db_list = API.delete_db(first_db_uuid, DataMySql.sid)
        Checking.check_status_code(result_post_db_list, 200)

    @allure.sub_suite('Complex')
    def test_complex(self):
        API.check_full_cycle(DataMySql.sid)

    def test_connect_my_sql(self):
        try:
            connection = mysql.connector.connect(host=DataMySql().data_to_connect_my_sql()['host'],
                                                 port=3306,
                                                 user=DataMySql().data_to_connect_my_sql()['user_name'],
                                                 database=DataMySql().data_to_connect_my_sql()['db_name'],
                                                 password=DataMySql().data_to_connect_my_sql()['password_db']
                                                 )
            print('Successfully connected...')
            try:
                with connection.cursor() as cursor:
                    cursor.execute('''
                    select 1 from dual''')
                    res = cursor.fetchall()
                    print(res)
            finally:
                connection.close()

            return connection
        except Exception as ex:
            print('Connection refused...')
            print(ex)

# body3 = {"dbtype": 3, "dbversion": 5, "env": 3, "region": 3}
# x = json.dumps(body3)
# print(sid)
# print(type(sid))
# result3 = requests.post('https://dbend.areso.pro/db_create', data=x, cookies=sid)
# print(result3.text)
