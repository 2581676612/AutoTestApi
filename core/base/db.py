import os.path
import sqlite3
from core.base.report import Report
from core.base.logger import logger


class DataBase():
    def __init__(self):
        self.path = Report.report_path
        self.file = os.path.join(self.path, 'api_result.db')
        self.conn = self._connect()
        self.cursor = self.conn.cursor()

    def _connect(self):
        """连接数据库"""
        return sqlite3.connect(self.file)

    def create_table(self, table='result', arg_dict={'api': 'varchar(20)','code': 'int','data': 'text'}):
        """创建表"""
        arg_str = ''
        for k, v in arg_dict.items():
            arg_str += f'{k} {v}, '
        self.cursor.execute(f'create table {table} ({arg_str[:-2]})')

    def insert_data(self, table, key=(), val=()):
        """写入数据"""
        sql = f'insert into {table} {key} values {val}'
        self.cursor.execute(sql)

    def commit(self):
        """提交修改"""
        self.cursor.close()
        self.conn.commit()
        self.conn.close()

DB = DataBase()