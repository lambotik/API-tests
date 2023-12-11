import json
import os

import requests
from dotenv import load_dotenv

from utils.request import API


class DataMySql:
    base_url = 'https://dbend.areso.pro'  # Base url
    load_dotenv()
    email = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')
    body = {"email": f'{email}', "password": f'{password}'}

    result = requests.post('https://dbend.areso.pro/login', json=body)
    # db_uuid = {"db_uuid": "0655bc53-db5b-7762-8000-4fe80aae1b4f"}
    # del_db = requests.post('https://dbend.areso.pro/db_delete', data=json_db_uuid, cookies=sid)
    # print(del_db.text)
    # json_db_uuid = json.dumps(db_uuid)

    sid = dict(result.cookies)
    print(sid)

    def data_to_connect_my_sql(self):
        list_db = API.post_db_list(self.sid)
        json_list_db = json.loads(list_db.text)
        first_db_uuid = list(json_list_db['content'].keys())[0]
        print(json_list_db['content'][first_db_uuid][3].split(':'))
        db_name = json_list_db['content'][first_db_uuid][0]
        print(db_name)
        user_name = json_list_db['content'][first_db_uuid][3].split(':')[1].replace('//', '')
        print(user_name)
        host = json_list_db['content'][first_db_uuid][3].split(':')[2].partition('@')[2]
        print(host)
        password_db = json_list_db['content'][first_db_uuid][3].split(':')[2].partition('@')[0]
        print(password_db)
        return {'host': host, 'user_name': user_name, 'db_name': db_name, 'password_db': password_db}
