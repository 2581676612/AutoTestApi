import os
from core.base.md5_encryption import *

#  app密钥
app_secret = 'qEuQUObml3nuwf7y'
timestamp = get_timestamp()
app_token = md5_encode(app_secret, timestamp)
#  文件夹绝对路径
main_path = os.path.dirname(__file__)
#  参数文件参数对应列数
column_dict = {
    'api': 1,
    'method': 2,
    'json': 3,
    'verify': 4
}