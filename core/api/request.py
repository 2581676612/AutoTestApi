import requests
import json as complexjson
from core.base.parse_config import request_url, table
from core.base.logger import logger
from core.base.db import DB
from global_args import *


class RequestApi():
    def __init__(self):
        self.headers = {'timestamp': timestamp,
                        'appSerectToken': app_token,
                        'Origin': 'https://www.yueliu.cn',
                        'Referer': 'https://www.yueliu.cn/'
                        }

    def request(self, url, method, json=None, verify_rule=None, **kwargs):
        api_url = request_url + url
        json = self.check_verify(verify_rule, json)
        self.request_log(url, method, json, self.headers)
        if method == "GET":
            if json:
                args_str = '?'
                for k, v in json.items():
                    args_str += f'{k}={v}&'
                api_url += args_str
            res = requests.get(api_url, headers=self.headers, **kwargs)
        elif method == "POST":
            res = requests.post(api_url, json=json, headers=self.headers, **kwargs)
        elif method == "PUT":
            # PUT 和 PATCH 中没有提供直接使用json参数的方法，因此需要用data来传入
            data = complexjson.dumps(json)
            res = requests.put(api_url, data, headers=self.headers, **kwargs)
        elif method == "DELETE":
            res = requests.delete(api_url, headers=self.headers, **kwargs)
        elif method == "PATCH":
            data = complexjson.dumps(json)
            res = requests.patch(api_url, data, headers=self.headers, **kwargs)
        else:
            logger.error('method参数异常！！！')
            assert 0
        logger.info(f'请求结果：{res.json()}')
        if res.json()['code'] == 1000 and 'login' in url:
            self.headers['authorization'] = res.json()['data']['token']
        self.write_result(url, res)
        if res.json()['code'] != 1000:
            logger.error('接口测试异常')
            assert 0
        return res.json()

    @staticmethod
    def request_log(url, method, json, header):
        space = ' ' * 28
        log = f"""请求接口：{url}\n{space}请求方式：{method}\n{space}请求头：{header}\n{space}请求数据：{json}"""
        logger.info(log)

    @staticmethod
    def write_result(api, res):
        """写入结果到数据库中"""
        res_code = res.json()['code']
        res_data = res.json()['data']
        res_msg = res.json()['msg']
        DB.insert_data(table=table, key=('api', 'code', 'data', 'msg'), val=(api, res_code, str(res_data), res_msg))

    @staticmethod
    def check_verify(verify, json):
        """添加verify参数"""
        if verify:
            arg_list = verify.split('+')
            arg_list = [arg.strip() for arg in arg_list]
            verify_str = ''
            for arg in arg_list:
                if arg.lower() == 'app_token':
                    verify_str += app_token
                elif arg not in json:
                    logger.error(f'verify参数--{arg} 不在json数据内')
                    assert 0
                else:
                    verify_str += json[arg]
            json['verify'] = md5_encode(verify_str)
        return json

Request = RequestApi()
