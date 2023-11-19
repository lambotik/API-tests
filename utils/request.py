import json
import os

import allure

from utils.http_methods import HttpMethods
from dotenv import load_dotenv

base_url = 'https://dbend.areso.pro'  # Base url
load_dotenv()
email = os.getenv('EMAIL')
password = os.getenv('PASSWORD')
MY_EMAIL = os.getenv('EMAIL')
MY_PASSWORD = os.getenv('PASSWORD')


class API:
    @staticmethod
    def get_tos():
        get_resource = '/tos'  # Resource for method GET
        get_url = base_url + get_resource
        print(get_url)
        result_get = HttpMethods.get(get_url)
        with allure.step(f'Body: {result_get.text}'):
            print(result_get.text)
        return result_get

    @staticmethod
    def get_list_dbtypes():
        get_resource = '/list_dbtypes'  # Resource for method GET
        get_url = base_url + get_resource
        print(get_url)
        result_get = HttpMethods.get(get_url)
        with allure.step(f'Body: {result_get.text}'):
            print(result_get.text)
        return result_get

    @staticmethod
    def get_list_dbversions():
        get_resource = '/list_dbversions'  # Resource for method GET
        get_url = base_url + get_resource
        print(get_url)
        result_get = HttpMethods.get(get_url)
        with allure.step(f'Body: {result_get.text}'):
            print(result_get.text)
        return result_get

    @staticmethod
    def get_list_envs():
        get_resource = '/list_envs'  # Resource for method GET
        get_url = base_url + get_resource
        print(get_url)
        result_get = HttpMethods.get(get_url)
        with allure.step(f'Body: {result_get.text}'):
            print(result_get.text)
        return result_get

    @staticmethod
    def get_list_regions():
        get_resource = '/list_regions'  # Resource for method GET
        get_url = base_url + get_resource
        print(get_url)
        result_get = HttpMethods.get(get_url)
        with allure.step(f'Body: {result_get.text}'):
            print(result_get.text)
        return result_get

    @staticmethod
    def post_registration():
        """
        Method for create new user
        :return: JSON Response
        """
        json_for_create_new_user = {"email": email, "password": password}

        post_resource = '/register'  # Resource for method POST
        post_url = base_url + post_resource
        print(post_url)
        result_post = HttpMethods.post(post_url, json_for_create_new_user)
        with allure.step(f'Body: {result_post.text}'):
            print('Response body: ', result_post.text)
        return result_post

    @staticmethod
    def post_login(body: dict):
        post_resource = '/login'  # Resource for method GET
        post_url = base_url + post_resource
        print(post_url)
        result_post = HttpMethods.post(post_url, body)
        cookies = result_post.cookies
        print(f'Cookies: {cookies}')
        sid = result_post.cookies.values()[0]
        with allure.step('Body: {"email":"your_email","password":"your_password"}'):
            print('Response: ', result_post, f'Sid: {sid}')
        print(f'Sid: {sid}')
        return result_post, sid

    @staticmethod
    def post_db_list(sid: dict):
        """
        :param sid:
        :return:
        """
        post_resource = '/db_list'  # Resource for method
        post_url = base_url + post_resource
        print(post_url)
        result_post = HttpMethods.post_set_cookie(post_url, {}, sid)
        with allure.step(f'Body: {result_post.text}'):
            print('Response: ', result_post.text)
        return result_post

    @staticmethod
    def post_db_create(sid: dict):
        post_resource = '/db_create'  # Resource for method
        post_url = base_url + post_resource
        print(post_url)
        body = {"dbtype": 3, "dbversion": 5, "env": 3, "region": 3}
        result_post = HttpMethods.post_set_cookie_without_body(post_url, sid, body)
        with allure.step(f'Body: {result_post.text}'):
            print('Response: ', result_post.text)
        return result_post

    @staticmethod
    def put_default_user(user_id):
        """
        Method for changing new location
        :param user_id: int
        :return: JSON Response
        """
        put_resource = 'api/users/'  # Resource for method PUT
        put_url = base_url + put_resource + user_id
        print(put_url)
        json_for_update_new_place = \
            {
                "name": 'morpheus',
                "job": "zion resident"
            }
        result_put = HttpMethods.put(put_url, json_for_update_new_place)
        print('Response body: ', result_put.text)
        return result_put

    @staticmethod
    def delete_new_user(user_id):
        """
        Method delete user
        :param user_id:
        :return: JSON Response
        """
        delete_resource = 'api/users/'  # Resource for method DELETE
        delete_url = base_url + delete_resource + user_id
        print('Url: ', delete_url)
        json_for_delete_new_user = {"id": user_id}
        result_delete = HttpMethods.delete(delete_url, json_for_delete_new_user)
        with allure.step('Response body:'):
            print('Response body: ', result_delete.text)
        return result_delete

    @staticmethod
    def checking_unknown_user(user_id):
        get_resource = 'api/unknown/'  # Resource for method GET
        get_url = base_url + get_resource + user_id
        print(get_url)
        result_get = HttpMethods.get(get_url)
        print(result_get.text)
        return result_get
