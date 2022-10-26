import pytest
from core.base.parse_data import DataFile
from core.api.request import Request

file_name = 'data.xlsx'
data_file = DataFile(file_name)  # 可传入sheet参数指定表
row_list = data_file.parse_file()
data_file.close_file()
api_list = [row[0] for row in row_list]


@pytest.mark.parametrize('row', row_list, ids=api_list)
def test_file(row):
    """接口测试"""
    res = Request.request(url=row[0],
                          method=row[1].upper(),
                          json=row[2])

if __name__ == '__main__':
    pytest.main(['test_data_file.py', '-sv'])
