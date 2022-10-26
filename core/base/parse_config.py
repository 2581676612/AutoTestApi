import configparser
import os
import json
from global_args import main_path

config = configparser.ConfigParser()
config.read(os.path.join(main_path, 'config.cfg'))

request_url = config.get('Env', 'request_url')

case = config.get('TestCase', 'case')

#数据库相关
table = config.get('DB', 'table')
arg_dict = json.loads(config.get('DB', 'arg_dict'))
