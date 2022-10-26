from core.api.request import Request


class TestCase():
    def test_demo(self):
        """测试用例模版"""
        res = Request.request(url='/api/company/login',
                              method='POST',
                              json={'phone': '18612031549', 'email': '', 'platform': 1, 'code': '',
                                    'password': 'youhongyang12345'},
                              verify_rule='app_token + phone + email + code + password'
                              )
        # Request.check_data()  # 检测结果【暂未开发】
