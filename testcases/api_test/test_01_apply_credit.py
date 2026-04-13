import allure
import pytest

from common.logger import logger
from testcases.conftest import api_data
from operation.credit import post_apply_credit
from common.assertions import assert_api_response

def get_case_name(test_data):
    """从测试数据字典中提取用例名称"""
    return test_data["name"]

@allure.epic("针对单个接口的测试")
@allure.feature("获取用户信息模块")
class TestCreditApply:  # 类名改为更贴切的名称




    @allure.story("用例--授信申请")
    @allure.description("该用例是针对授信申请接口的测试")
    @allure.issue("https://www.cnblogs.com/wintest", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.cnblogs.com/wintest", name="点击，跳转到对应用例的链接地址")
    @pytest.mark.single
    @pytest.mark.parametrize("test_data", api_data["test_apply_credit"], ids=get_case_name)
    def test_apply_credit(self, test_data):
        logger.info("*************** 开始执行用例 ***************")

        # 从参数中获取请求数据和预期结果
        request_data = test_data["request"]
        expect = test_data["expect"]
        # 调用操作层，传入动态请求数据
        result = post_apply_credit(request_data)
        # 断言
        assert_api_response(result, expect, test_data)
        logger.info("*************** 结束执行用例 ***************")

