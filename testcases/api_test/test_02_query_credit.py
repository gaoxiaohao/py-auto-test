import allure
import pytest

from common.assertions import assert_api_response
from testcases.conftest import api_data
from common.logger import logger
from operation.credit import post_query_credit

def get_data(query_data):
    return query_data["name"]

class TestCreditQuery:


    @allure.story("用例-授信结果查询")
    @allure.description("授信结果查询接口")
    @pytest.mark.single
    @pytest.mark.parametrize("query_data",api_data["test_query_creidt"],ids=get_data)
    def test_query_credit(self,query_data):
        logger.info("**********开始执行用例**********")
        request = query_data["request"]
        expect = query_data["expect"]
        result = post_query_credit(request)
        assert_api_response(result,expect,query_data)
        logger.info("*************** 结束执行用例 ***************")