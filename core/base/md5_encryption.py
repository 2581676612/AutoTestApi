import hashlib
import time


def get_timestamp():
    timestamp = round(time.time() * 1000)
    return str(timestamp)


def md5_encode(*param):
    param = [str(i) for i in param]
    str_val = ''.join(param)
    res = hashlib.md5(str_val.encode(encoding='utf-8'))
    return res.hexdigest()
